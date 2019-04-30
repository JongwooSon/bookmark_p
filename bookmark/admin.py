from django.contrib import admin
from .models import Bookmark

# Register your models here.

from .models import Bookmark

class BookmarkOptions(admin.ModelAdmin):
    list_display = ['id', 'site_name', 'url']
    # list_editable = ['site_name', 'url']
    list_filter = ['url'] # 대부분 DateTime 필드가 있을 경우 많이 사용
    search_fields = ['site_name', 'url'] # ForeignKey 필드같은 다른 테이블을 참조하는 항목은 X
    # raw_id_fields : 선택값 -> 입력값
    # 관리자 페이지에 커스텀 페이지 추가
    # 관리자 페이지에 action 추가



admin.site.register(Bookmark, BookmarkOptions)

