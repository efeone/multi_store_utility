frappe.ui.form.on("Stock Entry", {
  refresh: function (frm) {
    set_stock_entry_type_filter(frm);
  },
  outlet: function (frm) {
    set_warehouse_from_outlet(frm);
  },
});

/**
 * set filter for stock entry type field
 *
 * @param {object} frm - form object of stock entry
 */
function set_stock_entry_type_filter(frm) {
  frm.set_query("stock_entry_type", () => {
    return {
      filters: {
        name: ["in", ["Material Issue", "Material Receipt", "Material Consumption for Manufacture"]],
      },
    };
  });
}

/**
 * fetches and set warehouse from the selected outlet
 *
 * @param {object} frm - form object of stock entry
 */
function set_warehouse_from_outlet(frm) {
  if (frm.doc.outlet) {
    let default_source_warehouse = "";
    frappe.db.get_value("Outlet", frm.doc.outlet, "warehouse").then((r) => {
      default_source_warehouse = r.message.warehouse;
      frm.set_value("from_warehouse", default_source_warehouse);
    });
  }
}
