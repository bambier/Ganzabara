```
src/
├── main.py                      # Application entry point
├── app.py                       # QApplication subclass, central app
├── ui/
│   ├── __init__.py
│   ├── main_window.py           # MainWindow
│   ├── login_dialog.py
│   ├── navigation_sidebar.py
│   ├── dashboard_page.py
│   ├── invoices/                # all invoice-related views
│   │   ├── invoices_page.py
│   │   ├── invoice_list_view.py
│   │   ├── invoice_form_view.py
│   │   └── receipt_scan_view.py
│   ├── accounting/              # chart of accounts, journal, reports
│   │   ├── accounting_page.py
│   │   ├── chart_of_accounts_view.py
│   │   ├── journal_entry_view.py
│   │   └── financial_reports_view.py
│   ├── inventory/               # items, suppliers
│   │   ├── inventory_page.py
│   │   ├── item_list_view.py
│   │   ├── item_form_view.py
│   │   └── supplier_list_view.py
│   ├── payroll/                 # employees, payroll runs
│   │   ├── payroll_page.py
│   │   ├── employee_list_view.py
│   │   └── payroll_run_view.py
│   ├── banking/                 # bank feeds, reconciliation
│   │   ├── bank_page.py
│   │   ├── bank_feed_view.py
│   │   └── reconciliation_view.py
│   └── settings/                # all settings sub‑views
│       ├── settings_page.py
│       ├── general_settings_view.py
│       ├── theme_settings_view.py
│       ├── backup_settings_view.py
│       └── user_management_view.py
├── controllers/
│   ├── __init__.py
│   ├── base_controller.py
│   ├── invoice_controller.py
│   ├── transaction_controller.py
│   ├── account_controller.py
│   ├── report_controller.py
│   ├── inventory_controller.py
│   ├── payroll_controller.py
│   ├── bank_controller.py
│   ├── user_controller.py
│   └── theme_controller.py
├── services/
│   ├── __init__.py
│   ├── database_service.py
│   ├── encryption_service.py
│   ├── backup_service.py
│   ├── report_service.py
│   ├── ocr_service.py
│   └── bank_feed_service.py
├── models/
│   ├── __init__.py
│   ├── account.py
│   ├── transaction.py
│   ├── invoice.py
│   ├── inventory_item.py
│   ├── employee.py
│   ├── user.py
│   ├── etc.                    # all business entity classes
├── data_models/                 # Qt table/models for views
│   ├── __init__.py
│   ├── account_table_model.py
│   ├── invoice_table_model.py
│   ├── item_table_model.py
│   ├── employee_table_model.py
│   ├── user_table_model.py
│   ├── bank_transaction_table_model.py
│   ├── payroll_table_model.py
│   ├── journal_entry_table_model.py
│   └── account_tree_model.py
├── utils/
│   ├── __init__.py
│   ├── validators.py
│   ├── decorators.py
│   └── helpers.py
└── resources/
    ├── themes/                   # QSS stylesheets
    │   ├── light.qss
    │   └── dark.qss
    ├── icons/                    # application icons
    └── locales/                  # translation files (if needed)
```