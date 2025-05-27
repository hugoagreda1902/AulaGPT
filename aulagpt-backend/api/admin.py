from django.contrib import admin
from .models import User, Class, UserClass, Documents, Tests, TestQuestion, TestAnswer, Activity

# Registra el modelo User en el panel de administración de Django
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    # Campos que se mostrarán en la lista de usuarios en el admin
    list_display = ('user_id', 'name', 'surname', 'email', 'role')
    # Permite buscar usuarios por nombre, apellido o correo electrónico
    search_fields = ('name', 'surname', 'email')
    # Añade un filtro lateral para filtrar usuarios según su rol (student o teacher)
    list_filter = ('role',)

@admin.register(Class)
class ClassAdmin(admin.ModelAdmin):
    list_display = ('class_id', 'class_name', 'acces_code')
    search_fields = ('class_name',)
    list_filter = ('acces_code',)


@admin.register(UserClass)
class UserClassAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'class_id')
    search_fields = ('class_id',)

@admin.register(Documents)
class DocumentsAdmin(admin.ModelAdmin):
    list_display = ('document_id', 'class_id', 'file_name', 'file_type', 'upload_date', 'drive_link')
    search_fields = ('file_name', 'document_id')
    list_filter = ('upload_date',)

@admin.register(Tests)
class TestsAdmin(admin.ModelAdmin):
    list_display = ('test_id', 'user_id', 'document_id', 'test_name', 'creation_date')
    search_fields = ('test_name', 'document_id')
    list_filter = ('creation_date',)

@admin.register(TestQuestion)
class TestQuestionAdmin(admin.ModelAdmin):
    list_display = ('question_id', 'test_id', 'question_text', 'option_1', 'option_2', 'option_3', 'correct_option')
    search_fields = ('question_text',)
    list_filter = ('test_id',)

@admin.register(TestAnswer)
class TestAnswerAdmin(admin.ModelAdmin):
    list_display = ('answer_id', 'user', 'test', 'question', 'selected_option', 'is_correct', 'answer_date')
    search_fields = ('user',)
    list_filter = ('test',)

@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ('activity_id', 'user', 'activity_type', 'timestamp')
    search_fields = ('user', 'activity_type')
    list_filter = ('timestamp',)
