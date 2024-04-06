import frappe


def create_material_receipt_against_target_outlet(doc, method=None):
    """method created a material receipt for the target outlet of a material issue

    Args:
        doc (StockEntry obj): document object of Stock Entry doctype
        method (str, optional): defines method of method call. Defaults to None.
    """
    # checking if the stock entry is material issue
    if doc.stock_entry_type == "Material Issue":
        # creating object of material receipt
        new_material_recept = frappe.new_doc("Stock Entry")
        new_material_recept.stock_entry_type = "Material Receipt"

        # fetching warehouse from target outlet
        target_warehouse = frappe.db.get_value(
            "Outlet", doc.custom_target_outlet, "warehouse"
        )

        new_material_recept.outlet = doc.custom_target_outlet
        new_material_recept.to_warehouse = target_warehouse

        for item in doc.items:
            new_material_recept.append(
                "items",
                {
                    # only need to these because the rest gets fetched
                    "t_warehouse": target_warehouse,
                    "item_code": item.item_code,
                    "qty": item.qty,
                },
            )

        # inserting the stock entry
        new_material_recept.insert(ignore_permissions=True)

        # sending notfiication to stock users
        if frappe.db.exists("Stock Entry", new_material_recept.name):
            # getting users from outlet
            users = frappe.db.get_list(
                "Portal User", {"parent": new_material_recept.outlet}, pluck="user"
            )
            for user in users:
                # checking if a user is stock user
                if frappe.utils.has_common(["Stock User"], frappe.get_roles(user)):
                    subject = "New Material Receipt created for {0}".format(
                        new_material_recept.outlet
                    )
                    # sending notification
                    create_notification_log(
                        new_material_recept.doctype,
                        new_material_recept.name,
                        user,
                        subject,
                    )


def create_notification_log(
    doctype, docname, recipient, subject, content=None, type=None
):
    """Creates a notification log in the database which will send a notification to the receipient

    Args:
        doctype (str): doctype of the referenced document
        docname (str): name of the referenced document
        recipient (str): name of the receipient user
        subject (str): subject of the notification
        content (str, optional): content/body of the notification. Defaults to None.
        type (str, optional): type of notification, can be Mention or Alert. Defaults to None.
    """
    notification_log = frappe.new_doc("Notification Log")
    notification_log.type = "Mention"
    if type:
        notification_log.type = type
    notification_log.document_type = doctype
    notification_log.document_name = docname
    notification_log.for_user = recipient
    notification_log.subject = subject
    if content:
        notification_log.email_content = content
    notification_log.save(ignore_permissions=True)
