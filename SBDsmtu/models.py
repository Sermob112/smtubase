from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.models.signals import post_migrate
# Create your models here.
class Purchase(models.Model):
    Id = models.AutoField(primary_key=True, verbose_name="Идентификатор")
    PurchaseOrder = models.CharField(null=True,blank=True, max_length=255, default="Нет данных", verbose_name="Закон")
    RegistryNumber = models.CharField(null=True,blank=True, max_length=255, default="Нет данных",  verbose_name="Реестровый номер")
    ProcurementMethod = models.CharField(null=True,blank=True, max_length=255, default="Нет данных", verbose_name="Метод закупки")
    PurchaseName = models.CharField(null=True,blank=True, max_length=255, default="Нет данных", verbose_name="Наименование закупки")
    AuctionSubject = models.CharField(null=True,blank=True, max_length=255, default="Нет данных", verbose_name="Предмет аукциона")
    PurchaseIdentificationCode = models.CharField(null=True,blank=True, max_length=255, default="Нет данных", verbose_name="Код идентификации закупки")
    LotNumber = models.IntegerField(null=True, default="Нет данных", verbose_name="Номер лота")
    LotName = models.CharField(null=True, max_length=255,blank=True, default="Нет данных", verbose_name="Наименование лота")
    InitialMaxContractPrice = models.FloatField(null=True,blank=True, default="Нет данных", verbose_name="Начальная максимальная цена контракта")
    Currency = models.CharField(null=True, blank=True,max_length=255, default="Нет данных", verbose_name="Валюта")
    InitialMaxContractPriceInCurrency = models.FloatField(null=True,blank=True, default="Нет данных", verbose_name="Начальная максимальная цена контракта в валюте")
    ContractCurrency = models.CharField(null=True,blank=True, max_length=255, default="Нет данных", verbose_name="Валюта контракта")
    OKDPClassification = models.CharField(null=True, blank=True,max_length=255, default="Нет данных", verbose_name="Классификация ОКДП")
    OKPDClassification = models.CharField(null=True,blank=True, max_length=255, default="Нет данных", verbose_name="Классификация ОКПД")
    OKPD2Classification = models.CharField(null=True, blank=True,max_length=255, default="Нет данных", verbose_name="Классификация ОКПД2")
    PositionCode = models.CharField(null=True,blank=True, max_length=255, default="Нет данных", verbose_name="Код позиции")
    CustomerName = models.CharField(null=True, blank=True,max_length=255, default="Нет данных", verbose_name="Наименование заказчика")
    ProcurementOrganization = models.CharField(null=True,blank=True, max_length=255, default="Нет данных", verbose_name="Организация закупки")
    PlacementDate = models.DateField(null=True,blank=True, default="Нет данных", verbose_name="Дата размещения")
    UpdateDate = models.DateField(null=True,blank=True, default="Нет данных", verbose_name="Дата обновления")
    ProcurementStage = models.CharField(null=True, blank=True,max_length=255, default="Нет данных", verbose_name="Этап закупки")
    ProcurementFeatures = models.CharField(null=True,blank=True, max_length=255, default="Нет данных", verbose_name="Особенности закупки")
    ApplicationStartDate = models.DateField(null=True,blank=True, default="Нет данных", verbose_name="Дата начала заявки")
    ApplicationEndDate = models.DateField(null=True, blank=True,default="Нет данных", verbose_name="Дата окончания заявки")
    AuctionDate = models.DateField(null=True,blank=True, default="Нет данных", verbose_name="Дата аукциона")

     # Добавленные поля
    
    QueryCount = models.IntegerField(null=True, blank=True,default="Нет данных", verbose_name="Количество запросов")
    ResponseCount = models.IntegerField(null=True, blank=True, default="Нет данных",verbose_name="Количество ответов") 
    additional_info = models.JSONField(null=True, blank=True,default="Нет данных", verbose_name="Дополнительная информация")    
    AveragePrice = models.FloatField(null=True, blank=True, default="Нет данных",verbose_name="Среднее значение цены")
    MinPrice = models.FloatField(null=True, blank=True, default="Нет данных",verbose_name="Минимальная цена")
    MaxPrice = models.FloatField(null=True, blank=True,default="Нет данных", verbose_name="Максимальная цена")
    StandardDeviation = models.FloatField(null=True, blank=True,default="Нет данных", verbose_name="Среднее квадратичное отклонение")
    CoefficientOfVariation = models.FloatField(null=True, blank=True, default="Нет данных",verbose_name="Коэффициент вариации")
    NMCKMarket = models.FloatField(null=True, blank=True,default="Нет данных", verbose_name="НМЦК рыночная")
    FinancingLimit = models.FloatField(null=True, blank=True,default="Нет данных", verbose_name="Лимит финансирования")

    def set_tkp(self, tkp_number, value):
        # Метод для установки значения TKP в дополнительной информации
        if self.additional_info is None:
            self.additional_info = {}
        self.additional_info[f"TKP{tkp_number}"] = value
        self.save()

    def get_tkp(self, tkp_number):
        # Метод для получения значения TKP из дополнительной информации
        if self.additional_info is None:
            return None
        return self.additional_info.get(f"TKP{tkp_number}")

    def remove_tkp(self, tkp_number):
        # Метод для удаления значения TKP из дополнительной информации
        if self.additional_info is not None and f"TKP{tkp_number}" in self.additional_info:
            del self.additional_info[f"TKP{tkp_number}"]
            self.save()




    
class Role(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="Идентификатор")
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    roles = models.ManyToManyField(Role)

    def __str__(self):
        return self.user.username 
    

@receiver(post_save, sender=User)
def set_user_role(sender, instance, created, **kwargs):
    if created:
        user_profile, _ = UserProfile.objects.get_or_create(user=instance)
        user_role, _ = Role.objects.get_or_create(name="Пользователь")
        user_profile.roles.add(user_role)

@receiver(post_migrate)
def create_default_roles_and_user(sender, **kwargs):
    if sender.name == "smtubase":  # Замените "your_app_name" на имя вашего приложения
        # Создаем роли, если их еще нет
        roles = ['Пользователь', 'Редактор', 'Администратор']
        for role in roles:
            Role.objects.get_or_create(name=role)

        # Создаем пользователя с ролью Администратор
        admin_role = Role.objects.get(name='Администратор')
        admin_user, created = User.objects.get_or_create(username='root', is_superuser=True, is_staff=True)
        admin_user.set_password('sa')
        admin_user.save()
        UserProfile.objects.get_or_create(user=admin_user)
        admin_user.userprofile.roles.add(admin_role)

    # def formatted_placement_date(self):
    #     return self.PlacementDate.strftime('%d.%m.%y') if self.PlacementDate else "Нет данных"

    # def formatted_update_date(self):
    #     return self.UpdateDate.strftime('%d.%m.%y') if self.UpdateDate else "Нет данных"

    # def formatted_application_start_date(self):
    #     return self.ApplicationStartDate.strftime('%d.%m.%y') if self.ApplicationStartDate else "Нет данных"

    # def formatted_application_end_date(self):
    #     return self.ApplicationEndDate.strftime('%d.%m.%y') if self.ApplicationEndDate else "Нет данных"

    # def formatted_auction_date(self):
    #     return self.AuctionDate.strftime('%d.%m.%y') if self.AuctionDate else "Нет данных"
    # TKP1 = models.FloatField(null=True, blank=True, verbose_name="ТКП1")
    # TKP2 = models.FloatField(null=True, blank=True, verbose_name="ТКП2")
    # TKP3 = models.FloatField(null=True, blank=True, verbose_name="ТКП3")
