from ninja import Router
from typing import List
from .models import WaitlistEntry
from .schemas import WaitlistEntryListSchema, WaitlistEntryDetailSchema, WaitlistEntryCreateSchema
from django.shortcuts import get_object_or_404
from ninja_jwt.authentication import JWTAuth

router = Router()
#/api/waitlists/
@router.get("", response=List[WaitlistEntryListSchema], auth =JWTAuth() )
def list_waitlist_entries(request):
  qs = WaitlistEntry.objects.all()
  return qs

#/api/waitlists/
@router.post("",response=WaitlistEntryDetailSchema)
def create_waitlist_entry(request,data:WaitlistEntryCreateSchema):
  obj = WaitlistEntry.objects.create(**data.dict())
  print(request.user)
  return obj


@router.get("{entry_id}/", response=WaitlistEntryDetailSchema,auth =JWTAuth())
def get_waitlist_entry(request,entry_id:int):
  obj = get_object_or_404(WaitlistEntry, id=entry_id)
  return obj