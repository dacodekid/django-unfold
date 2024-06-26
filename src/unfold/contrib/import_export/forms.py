from import_export.forms import ExportForm as BaseExportForm
from import_export.forms import ImportForm as BaseImportForm
from unfold.widgets import SELECT_CLASSES, UnfoldAdminFileFieldWidget


class ImportForm(BaseImportForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["resource"].widget.attrs["class"] = " ".join(SELECT_CLASSES)
        self.fields["import_file"].widget = UnfoldAdminFileFieldWidget()
        self.fields["format"].widget.attrs["class"] = " ".join(SELECT_CLASSES)


class ExportForm(BaseExportForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["resource"].widget.attrs["class"] = " ".join(SELECT_CLASSES)
        self.fields["format"].widget.attrs["class"] = " ".join(SELECT_CLASSES)
