from dataclasses import dataclass


@dataclass
class PartnerCardInfo:
    id: int
    type_name: str
    partner_name: str
    first_name: str
    last_name: str
    middle_name: str | None
    email: str
    phone_partner: str
    address: str
    inn_number: str
    rating: int
    discount: int


@dataclass
class PartnerUpdateDTO:
    id: int
    type_id: int
    partner_name: str
    first_name: str
    last_name: str
    middle_name: str | None
    email: str
    phone_partner: str
    address: str
    inn_number: str
    rating: int


@dataclass
class PartnerAddDTO:
    type_id: int
    partner_name: str
    first_name: str
    last_name: str
    middle_name: str | None
    email: str
    phone_partner: str
    address: str
    inn_number: str
    rating: int
