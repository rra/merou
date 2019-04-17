from typing import TYPE_CHECKING

from itests.pages.base import BaseElement, BasePage

if TYPE_CHECKING:
    from typing import List, Optional


class PermissionViewPage(BasePage):
    @property
    def description(self):
        # type: () -> Optional[str]
        descriptions = self.find_elements_by_class_name("permission-description")
        return descriptions[0].text if descriptions else None

    @property
    def has_audited_warning(self):
        # type: () -> bool
        warnings = self.find_elements_by_class_name("alert-warning")
        for warning in warnings:
            if "audited permission" in warning.text:
                return True
        return False

    @property
    def has_disable_auditing_button(self):
        # type: () -> bool
        return self.find_elements_by_class_name("disable-auditing") != []

    @property
    def has_disable_permission_button(self):
        # type: () -> bool
        return self.find_elements_by_class_name("disable-permission") != []

    @property
    def has_enable_auditing_button(self):
        # type: () -> bool
        return self.find_elements_by_class_name("enable-auditing") != []

    @property
    def has_no_grants(self):
        # type: () -> bool
        return self.find_elements_by_class_name("no-grants") != []

    @property
    def permission_grant_rows(self):
        # type: () -> List[PermissionViewGrantRow]
        all_permission_grant_rows = self.find_elements_by_class_name("grant-row")
        return [PermissionViewGrantRow(row) for row in all_permission_grant_rows]


class PermissionViewGrantRow(BaseElement):
    @property
    def argument(self):
        # type: () -> str
        return self.find_element_by_class_name("grant-argument").text

    @property
    def group(self):
        # type: () -> str
        return self.find_element_by_class_name("grant-group").text