import frappe

@frappe.whitelist()
def get_dimensions(with_cost_center_and_project=False):

    c = frappe.qb.DocType("Accounting Dimension Detail")
    p = frappe.qb.DocType("Accounting Dimension")
    dimension_filters = (
        frappe.qb.from_(p)
        .select(p.label, p.fieldname, p.document_type)
        .where(p.disabled == 0)
        .run(as_dict=1)
    )
    default_dimensions = (
        frappe.qb.from_(c)
        .inner_join(p)
        .on(c.parent == p.name)
        .select(p.fieldname, c.company, c.default_dimension)
        .run(as_dict=1)
    )

    if isinstance(with_cost_center_and_project, str):
        if with_cost_center_and_project.lower().strip() == "true":
            with_cost_center_and_project = True
        else:
            with_cost_center_and_project = False

    if with_cost_center_and_project:
        dimension_filters.extend(
            [
                {"fieldname": "cost_center", "document_type": "Cost Center"},
                {"fieldname": "project", "document_type": "Project"},
            ]
        )

    default_dimensions_map = {}
    for dimension in default_dimensions:
        default_dimensions_map.setdefault(dimension.company, {})
        if frappe.session.user != 'Administrator':
            user_permission = frappe.get_all("User Permission",
                                              filters={"user": frappe.session.user,
                                                       "allow": "Outlet"},
                                              fields=["for_value"],
                                              limit=1)
            if user_permission:
                outlet_name = user_permission[0].get("for_value")
                default_dimensions_map[dimension.company][dimension.fieldname] = outlet_name
            else:
                default_dimensions_map[dimension.company][dimension.fieldname] = dimension.default_dimension
        else:
            default_dimensions_map[dimension.company][dimension.fieldname] = dimension.default_dimension

    return dimension_filters, default_dimensions_map
