from enum import Enum


class StrEnum(str, Enum):
    """Enum where members are also (and must be) strs"""

    def __str__(self):
        return self.value

class CrmIdCode(StrEnum):
    CIF = "cif"
    NIF = "nif"
    NIE = "nie"
    PASSPORT = "passport"
    EUID = 'eqid'

class CrmIdDescription(StrEnum):
    CIF = "cif"
    NIF = "nif"
    NIE = "nie"
    PASSPORT = "passport"
    EUID = 'eqid'

class StageDescription(StrEnum):
    DRAFT = "draft"
    CUSTOMER_ACCOUT_CREATED = "customer_account_created"
    BASKET_CREATED = "batch_created"
    CARD_REGISTERED = "card_registered"
    DOCUMENTS_UPLOADED = 'documents_uploaded'
    REGISTRATION_COMPLETED = 'registration_completed'

CRM_ID_CODE = (
    (CrmIdCode.CIF, "CIF"),
    (CrmIdCode.NIF, "NIF"),
    (CrmIdCode.NIE, "NIE"),
    (CrmIdCode.PASSPORT, "PASSPORT"),
    (CrmIdCode.EUID, "EUID")
)

CRM_ID_DESCRIPTION = (
    (CrmIdDescription.CIF, "CIF"),
    (CrmIdDescription.NIF, "NIF"),
    (CrmIdDescription.NIE, "NIE"),
    (CrmIdDescription.PASSPORT, "PASSPORT"),
    (CrmIdDescription.EUID, "EUID")
)

STAGE_DESCRIPTION = (
    (StageDescription.DRAFT, "DRAFT"),
    (StageDescription.CUSTOMER_ACCOUT_CREATED, "CUSTOMER_ACCOUT_CREATED"),
    (StageDescription.BASKET_CREATED, "BASKET_CREATED"),
    (StageDescription.CARD_REGISTERED, "CARD_REGISTERED"),
    (StageDescription.DOCUMENTS_UPLOADED, "DOCUMENTS_UPLOADED"),
    (StageDescription.REGISTRATION_COMPLETED, "REGISTRATION_COMPLETED"),
)