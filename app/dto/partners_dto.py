from dataclasses import dataclass


@dataclass
class PartnersInfo:
    id: int
    type_name: str
    partner_name: str
    first_name_director: str
    last_name_director: str
    middle_name_director: str
    phone_partner: str
    rating: int
    discount: float


@dataclass
class PartnerUpdateDto:
    id: int
    partner_type_id: int
    partner_name: str
    first_name: str
    last_name: str
    middle_name: str
    email: str
    phone: str
    address: str
    inn: str
    rating: int
