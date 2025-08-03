  
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AvsAccounttypes(models.Model):
    code = models.IntegerField(db_column='Code', primary_key=True)  # Field name made lowercase.
    assistanttitle = models.CharField(db_column='AssistantTitle', max_length=50, blank=True, null=True)  # Field name made lowercase.
    detailtitle = models.CharField(db_column='DetailTitle', max_length=50, blank=True, null=True)  # Field name made lowercase.
    typegroup = models.IntegerField(db_column='TypeGroup', blank=True, null=True)  # Field name made lowercase.
    typesetting = models.IntegerField(db_column='TypeSetting', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AVS_AccountTypes'


class AvsAggregatetypes(models.Model):
    code = models.IntegerField(db_column='Code', primary_key=True)  # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=50, blank=True, null=True)  # Field name made lowercase.
    typegroup = models.IntegerField(db_column='TypeGroup', blank=True, null=True)  # Field name made lowercase.
    typesetting = models.IntegerField(db_column='TypeSetting', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AVS_AggregateTypes'


class AvsCurrencytypes(models.Model):
    code = models.IntegerField(db_column='Code', primary_key=True)  # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=100, blank=True, null=True)  # Field name made lowercase.
    typegroup = models.IntegerField(db_column='TypeGroup', blank=True, null=True)  # Field name made lowercase.
    scriptvalue = models.CharField(db_column='ScriptValue', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    typesetting = models.IntegerField(db_column='TypeSetting', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AVS_CurrencyTypes'


class AvsGrouptypes(models.Model):
    code = models.IntegerField(db_column='Code', primary_key=True)  # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=50, blank=True, null=True)  # Field name made lowercase.
    partcode = models.IntegerField(db_column='PartCode', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AVS_GroupTypes'


class AvsSettingtypes(models.Model):
    code = models.IntegerField(db_column='Code', primary_key=True)  # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=50, blank=True, null=True)  # Field name made lowercase.
    typegroup = models.IntegerField(db_column='TypeGroup', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AVS_SettingTypes'


class Accassistants(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    code = models.SmallIntegerField(db_column='Code')  # Field name made lowercase.
    totalcode = models.SmallIntegerField(db_column='TotalCode', blank=True, null=True)  # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=100)  # Field name made lowercase.
    comment = models.CharField(db_column='Comment', max_length=500, blank=True, null=True)  # Field name made lowercase.
    createdtime = models.CharField(db_column='CreatedTime', max_length=5, blank=True, null=True)  # Field name made lowercase.
    createddate = models.CharField(db_column='CreatedDate', max_length=10, blank=True, null=True)  # Field name made lowercase.
    modifiedtime = models.CharField(db_column='ModifiedTime', max_length=5, blank=True, null=True)  # Field name made lowercase.
    modifieddate = models.CharField(db_column='ModifiedDate', max_length=10, blank=True, null=True)  # Field name made lowercase.
    usercreated = models.CharField(db_column='UserCreated', max_length=50, blank=True, null=True)  # Field name made lowercase.
    usermodified = models.CharField(db_column='UserModified', max_length=50, blank=True, null=True)  # Field name made lowercase.
    detailstype = models.SmallIntegerField(db_column='DetailsType')  # Field name made lowercase.
    isaffecttoroll = models.BooleanField(db_column='IsAffectToRoll')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AccAssistants'


class Accassistantsdetailsinterface(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    accassistantsid = models.IntegerField(db_column='AccAssistantsID')  # Field name made lowercase. The composite primary key (AccAssistantsID, AccDetailsCollectionID) found, that is not supported. The first column is selected.
    accdetailscollectionid = models.IntegerField(db_column='AccDetailsCollectionID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AccAssistantsDetailsInterface'
        unique_together = (('accassistantsid', 'accdetailscollectionid'),)


class Acccategoriesdt(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    acccategoriesmsid = models.ForeignKey('Acccategoriesms', on_delete=models.DO_NOTHING, db_column='AccCategoriesMSID')  # Field name made lowercase.
    createdtime = models.CharField(db_column='CreatedTime', max_length=5)  # Field name made lowercase.
    createddate = models.CharField(db_column='CreatedDate', max_length=10)  # Field name made lowercase.
    modifiedtime = models.CharField(db_column='ModifiedTime', max_length=5, blank=True, null=True)  # Field name made lowercase.
    modifieddate = models.CharField(db_column='ModifiedDate', max_length=10, blank=True, null=True)  # Field name made lowercase.
    usercreated = models.IntegerField(db_column='UserCreated')  # Field name made lowercase.
    usermodified = models.IntegerField(db_column='UserModified', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AccCategoriesDT'


class Acccategoriesms(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    code = models.IntegerField(db_column='Code', unique=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=256)  # Field name made lowercase.
    accdetailstypesid = models.ForeignKey('Accdetailstypes', on_delete=models.DO_NOTHING, db_column='AccDetailsTypesID')  # Field name made lowercase.
    filtertype = models.SmallIntegerField(db_column='FilterType')  # Field name made lowercase.
    ctequeryresult = models.TextField(db_column='CTEQueryResult', blank=True, null=True)  # Field name made lowercase.
    queryresult = models.TextField(db_column='QueryResult', blank=True, null=True)  # Field name made lowercase.
    comment = models.CharField(db_column='Comment', max_length=512, blank=True, null=True)  # Field name made lowercase.
    issystemrecord = models.BooleanField(db_column='IsSystemRecord')  # Field name made lowercase.
    createdtime = models.CharField(db_column='CreatedTime', max_length=5)  # Field name made lowercase.
    createddate = models.CharField(db_column='CreatedDate', max_length=10)  # Field name made lowercase.
    modifiedtime = models.CharField(db_column='ModifiedTime', max_length=5, blank=True, null=True)  # Field name made lowercase.
    modifieddate = models.CharField(db_column='ModifiedDate', max_length=10, blank=True, null=True)  # Field name made lowercase.
    usercreated = models.IntegerField(db_column='UserCreated')  # Field name made lowercase.
    usermodified = models.IntegerField(db_column='UserModified', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AccCategoriesMS'


class Acccategoriessubdt(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    acccategoriesdtid = models.ForeignKey(Acccategoriesdt, on_delete=models.DO_NOTHING, db_column='AccCategoriesDTID')  # Field name made lowercase.
    accdetailsfieldsinfoid = models.ForeignKey('Accdetailsfieldsinfo', on_delete=models.DO_NOTHING, db_column='AccDetailsFieldsInfoID')  # Field name made lowercase.
    comparetype = models.SmallIntegerField(db_column='CompareType')  # Field name made lowercase.
    value = models.CharField(db_column='Value', max_length=128)  # Field name made lowercase.
    createdtime = models.CharField(db_column='CreatedTime', max_length=5)  # Field name made lowercase.
    createddate = models.CharField(db_column='CreatedDate', max_length=10)  # Field name made lowercase.
    modifiedtime = models.CharField(db_column='ModifiedTime', max_length=5, blank=True, null=True)  # Field name made lowercase.
    modifieddate = models.CharField(db_column='ModifiedDate', max_length=10, blank=True, null=True)  # Field name made lowercase.
    usercreated = models.IntegerField(db_column='UserCreated')  # Field name made lowercase.
    usermodified = models.IntegerField(db_column='UserModified', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AccCategoriesSubDT'


class Acccrconvrate(models.Model):
    crratecode = models.IntegerField(db_column='CrRateCode', primary_key=True)  # Field name made lowercase.
    acccurrencyid = models.IntegerField(db_column='AccCurrencyID')  # Field name made lowercase.
    crratedate = models.CharField(db_column='CrRateDate', max_length=10)  # Field name made lowercase.
    crratetime = models.CharField(db_column='CrRateTime', max_length=5, blank=True, null=True)  # Field name made lowercase.
    crrateconvrate = models.DecimalField(db_column='CrRateconvRate', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    crratedesc = models.CharField(db_column='CrRateDesc', max_length=200, blank=True, null=True)  # Field name made lowercase.
    crratesymbol = models.CharField(db_column='CrRateSymbol', max_length=100, blank=True, null=True)  # Field name made lowercase.
    cractive = models.BooleanField(db_column='crACtive', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AccCrConvRate'


class Acccurrency(models.Model):
    curcode = models.IntegerField(db_column='CurCode', primary_key=True)  # Field name made lowercase.
    curtitle = models.CharField(db_column='CurTitle', max_length=100)  # Field name made lowercase.
    curcountry = models.CharField(db_column='CurCountry', max_length=100, blank=True, null=True)  # Field name made lowercase.
    curamount = models.DecimalField(db_column='CurAmount', max_digits=23, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    curdesc = models.CharField(db_column='CurDesc', max_length=200, blank=True, null=True)  # Field name made lowercase.
    cursymbol = models.CharField(db_column='CurSymbol', max_length=100, blank=True, null=True)  # Field name made lowercase.
    curbase = models.BooleanField(db_column='CurBase', blank=True, null=True)  # Field name made lowercase.
    totalcode = models.IntegerField(db_column='TotalCode', blank=True, null=True)  # Field name made lowercase.
    assistantcode = models.IntegerField(db_column='AssistantCode', blank=True, null=True)  # Field name made lowercase.
    detailcode = models.IntegerField(db_column='DetailCode', blank=True, null=True)  # Field name made lowercase.
    cursmallerunit = models.CharField(db_column='CurSmallerUnit', max_length=100)  # Field name made lowercase.
    decimalplacecount = models.SmallIntegerField(db_column='DecimalPlaceCount', blank=True, null=True)  # Field name made lowercase.
    currencytype = models.CharField(db_column='CurrencyType', max_length=3, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AccCurrency'


class Accdetailscoderanges(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    accdetailstypesid = models.ForeignKey('Accdetailstypes', on_delete=models.DO_NOTHING, db_column='AccDetailsTypesID')  # Field name made lowercase.
    acccodefrom = models.IntegerField(db_column='AccCodeFrom')  # Field name made lowercase.
    acccodeto = models.IntegerField(db_column='AccCodeTo')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AccDetailsCodeRanges'


class Accdetailscollection(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    accdetailstypesid = models.ForeignKey('Accdetailstypes', on_delete=models.DO_NOTHING, db_column='AccDetailsTypesID')  # Field name made lowercase.
    accdetailcode = models.IntegerField(db_column='AccDetailCode')  # Field name made lowercase.
    accountcode = models.IntegerField(db_column='AccountCode', unique=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=256)  # Field name made lowercase.
    currcode = models.IntegerField(db_column='CurrCode', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AccDetailsCollection'
        unique_together = (('accdetailstypesid', 'accdetailcode'),)


class Accdetailsfieldsinfo(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    accdetailstypesid = models.ForeignKey('Accdetailstypes', on_delete=models.DO_NOTHING, db_column='AccDetailsTypesID')  # Field name made lowercase.
    viewfieldname = models.CharField(db_column='ViewFieldName', max_length=128)  # Field name made lowercase.
    fieldname = models.CharField(db_column='FieldName', max_length=128)  # Field name made lowercase.
    fieldtype = models.SmallIntegerField(db_column='FieldType')  # Field name made lowercase.
    iscurrency = models.BooleanField(db_column='IsCurrency')  # Field name made lowercase.
    length = models.SmallIntegerField(db_column='Length', blank=True, null=True)  # Field name made lowercase.
    scale = models.SmallIntegerField(db_column='Scale', blank=True, null=True)  # Field name made lowercase.
    issimplefiltertype = models.SmallIntegerField(db_column='IsSimpleFilterType')  # Field name made lowercase.
    islookup = models.BooleanField(db_column='IsLookup')  # Field name made lowercase.
    lookuptablename = models.CharField(db_column='LookupTableName', max_length=128, blank=True, null=True)  # Field name made lowercase.
    lookupkeyfieldname = models.CharField(db_column='LookupKeyFieldName', max_length=128, blank=True, null=True)  # Field name made lowercase.
    lookupresultfieldname = models.CharField(db_column='LookupResultFieldName', max_length=128, blank=True, null=True)  # Field name made lowercase.
    lookupwhereclause = models.CharField(db_column='LookupWhereClause', max_length=512, blank=True, null=True)  # Field name made lowercase.
    uselookupquery = models.BooleanField(db_column='UseLookupQuery')  # Field name made lowercase.
    lookupquery = models.TextField(db_column='LookupQuery', blank=True, null=True)  # Field name made lowercase.
    islinkedquery = models.BooleanField(db_column='IsLinkedQuery')  # Field name made lowercase.
    linkedctequery = models.TextField(db_column='LinkedCTEQuery', blank=True, null=True)  # Field name made lowercase.
    linkedquery = models.TextField(db_column='LinkedQuery', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AccDetailsFieldsInfo'


class Accdetailsinterface(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    accassistantsid = models.ForeignKey(Accassistants, on_delete=models.DO_NOTHING, db_column='AccAssistantsID')  # Field name made lowercase.
    acccategoriesmsid = models.ForeignKey(Acccategoriesms, on_delete=models.DO_NOTHING, db_column='AccCategoriesMSID')  # Field name made lowercase.
    createdtime = models.CharField(db_column='CreatedTime', max_length=5)  # Field name made lowercase.
    createddate = models.CharField(db_column='CreatedDate', max_length=10)  # Field name made lowercase.
    modifiedtime = models.CharField(db_column='ModifiedTime', max_length=5, blank=True, null=True)  # Field name made lowercase.
    modifieddate = models.CharField(db_column='ModifiedDate', max_length=10, blank=True, null=True)  # Field name made lowercase.
    usercreated = models.IntegerField(db_column='UserCreated')  # Field name made lowercase.
    usermodified = models.IntegerField(db_column='UserModified', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AccDetailsInterface'


class Accdetailsstatic(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    code = models.IntegerField(db_column='Code')  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=512)  # Field name made lowercase.
    comment = models.CharField(db_column='Comment', max_length=512, blank=True, null=True)  # Field name made lowercase.
    createdtime = models.CharField(db_column='CreatedTime', max_length=5)  # Field name made lowercase.
    createddate = models.CharField(db_column='CreatedDate', max_length=10)  # Field name made lowercase.
    modifiedtime = models.CharField(db_column='ModifiedTime', max_length=5, blank=True, null=True)  # Field name made lowercase.
    modifieddate = models.CharField(db_column='ModifiedDate', max_length=10, blank=True, null=True)  # Field name made lowercase.
    usercreated = models.IntegerField(db_column='UserCreated')  # Field name made lowercase.
    usermodified = models.IntegerField(db_column='UserModified', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AccDetailsStatic'


class Accdetailstypes(models.Model):
    id = models.SmallIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    typename = models.CharField(db_column='TypeName', max_length=128)  # Field name made lowercase.
    typesingularname = models.CharField(db_column='TypeSingularName', max_length=128)  # Field name made lowercase.
    tablename = models.CharField(db_column='TableName', max_length=128)  # Field name made lowercase.
    isstaticaccount = models.BooleanField(db_column='IsStaticAccount')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AccDetailsTypes'


class Accgroups(models.Model):
    code = models.SmallIntegerField(db_column='Code', primary_key=True)  # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=100)  # Field name made lowercase.
    type = models.SmallIntegerField(db_column='Type')  # Field name made lowercase.
    comment = models.CharField(db_column='Comment', max_length=500, blank=True, null=True)  # Field name made lowercase.
    createdtime = models.CharField(db_column='CreatedTime', max_length=5, blank=True, null=True)  # Field name made lowercase.
    createddate = models.CharField(db_column='CreatedDate', max_length=10, blank=True, null=True)  # Field name made lowercase.
    modifiedtime = models.CharField(db_column='ModifiedTime', max_length=5, blank=True, null=True)  # Field name made lowercase.
    modifieddate = models.CharField(db_column='ModifiedDate', max_length=10, blank=True, null=True)  # Field name made lowercase.
    usercreated = models.CharField(db_column='UserCreated', max_length=50, blank=True, null=True)  # Field name made lowercase.
    usermodified = models.CharField(db_column='UserModified', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AccGroups'


class Accmixed(models.Model):
    kol = models.SmallIntegerField(blank=True, null=True)
    debit = models.DecimalField(db_column='Debit', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    credit = models.DecimalField(db_column='Credit', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    tafsili2 = models.IntegerField(db_column='Tafsili2', blank=True, null=True)  # Field name made lowercase.
    remainamount = models.DecimalField(db_column='RemainAmount', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    koltitle = models.CharField(db_column='KolTitle', max_length=100, blank=True, null=True)  # Field name made lowercase.
    remainstatus = models.CharField(db_column='RemainStatus', max_length=8)  # Field name made lowercase.
    accstatus = models.IntegerField(db_column='AccStatus')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AccMixed'


class Acctotals(models.Model):
    code = models.SmallIntegerField(db_column='Code', primary_key=True)  # Field name made lowercase.
    groupcode = models.ForeignKey(Accgroups, on_delete=models.DO_NOTHING, db_column='GroupCode')  # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=100)  # Field name made lowercase.
    assistanttype = models.SmallIntegerField(db_column='AssistantType', blank=True, null=True)  # Field name made lowercase.
    type = models.SmallIntegerField(db_column='Type', blank=True, null=True)  # Field name made lowercase.
    nature = models.SmallIntegerField(db_column='Nature', blank=True, null=True)  # Field name made lowercase.
    comment = models.CharField(db_column='Comment', max_length=500, blank=True, null=True)  # Field name made lowercase.
    createdtime = models.CharField(db_column='CreatedTime', max_length=5, blank=True, null=True)  # Field name made lowercase.
    createddate = models.CharField(db_column='CreatedDate', max_length=10, blank=True, null=True)  # Field name made lowercase.
    modifiedtime = models.CharField(db_column='ModifiedTime', max_length=5, blank=True, null=True)  # Field name made lowercase.
    modifieddate = models.CharField(db_column='ModifiedDate', max_length=10, blank=True, null=True)  # Field name made lowercase.
    usercreated = models.CharField(db_column='UserCreated', max_length=50, blank=True, null=True)  # Field name made lowercase.
    usermodified = models.CharField(db_column='UserModified', max_length=50, blank=True, null=True)  # Field name made lowercase.
    total_isaffecttoroll = models.BooleanField(db_column='Total_IsAffectToRoll', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AccTotals'


class Alterprice(models.Model):
    alterprice = models.IntegerField(db_column='AlterPrice', blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AlterPrice'


class Answers(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    code = models.IntegerField(db_column='Code')  # Field name made lowercase.
    answer = models.CharField(db_column='Answer', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    creatdate = models.DateTimeField(db_column='CreatDate', blank=True, null=True)  # Field name made lowercase.
    modifydate = models.DateTimeField(db_column='ModifyDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Answers'


class Appfeatures(models.Model):
    code = models.IntegerField(db_column='Code', primary_key=True)  # Field name made lowercase.
    parentcode = models.IntegerField(db_column='ParentCode', blank=True, null=True)  # Field name made lowercase.
    group = models.SmallIntegerField(db_column='Group', blank=True, null=True)  # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=100, blank=True, null=True)  # Field name made lowercase.
    enumtitle = models.CharField(db_column='EnumTitle', max_length=50, blank=True, null=True)  # Field name made lowercase.
    filecode = models.IntegerField(db_column='FileCode', blank=True, null=True)  # Field name made lowercase.
    procname = models.CharField(db_column='ProcName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    shortcut = models.IntegerField(db_column='Shortcut', blank=True, null=True)  # Field name made lowercase.
    password = models.BooleanField(db_column='Password')  # Field name made lowercase.
    keywords = models.CharField(db_column='Keywords', max_length=500, blank=True, null=True)  # Field name made lowercase.
    displayorder = models.SmallIntegerField(db_column='DisplayOrder', blank=True, null=True)  # Field name made lowercase.
    icon = models.SmallIntegerField(db_column='Icon', blank=True, null=True)  # Field name made lowercase.
    isnew = models.BooleanField(db_column='Isnew')  # Field name made lowercase.
    color = models.IntegerField(db_column='Color', blank=True, null=True)  # Field name made lowercase.
    size = models.SmallIntegerField(db_column='Size', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AppFeatures'


class Appfiles(models.Model):
    code = models.IntegerField(db_column='Code', primary_key=True)  # Field name made lowercase.
    filename = models.CharField(db_column='FileName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    version = models.DecimalField(db_column='Version', max_digits=23, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    file = models.BinaryField(db_column='File', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AppFiles'


class Appmenuitems(models.Model):
    code = models.IntegerField(db_column='Code', primary_key=True)  # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=100, blank=True, null=True)  # Field name made lowercase.
    filecode = models.IntegerField(db_column='FileCode', blank=True, null=True)  # Field name made lowercase.
    procname = models.CharField(db_column='ProcName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    parentcode = models.IntegerField(db_column='ParentCode', blank=True, null=True)  # Field name made lowercase.
    shortcut = models.IntegerField(db_column='Shortcut', blank=True, null=True)  # Field name made lowercase.
    password = models.BooleanField(db_column='Password')  # Field name made lowercase.
    keywords = models.CharField(db_column='Keywords', max_length=500, blank=True, null=True)  # Field name made lowercase.
    packages = models.CharField(db_column='Packages', max_length=50, blank=True, null=True)  # Field name made lowercase.
    subpackages = models.CharField(db_column='Subpackages', max_length=50, blank=True, null=True)  # Field name made lowercase.
    displayorder = models.SmallIntegerField(db_column='DisplayOrder', blank=True, null=True)  # Field name made lowercase.
    desktops = models.CharField(db_column='Desktops', max_length=50, blank=True, null=True)  # Field name made lowercase.
    icon = models.SmallIntegerField(db_column='Icon', blank=True, null=True)  # Field name made lowercase.
    id = models.CharField(db_column='ID', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    group = models.SmallIntegerField(db_column='Group', blank=True, null=True)  # Field name made lowercase.
    packages_x = models.CharField(db_column='Packages_X', max_length=50, blank=True, null=True)  # Field name made lowercase.
    subpackages_x = models.CharField(db_column='Subpackages_X', max_length=50, blank=True, null=True)  # Field name made lowercase.
    desktops_x = models.CharField(db_column='Desktops_X', max_length=50, blank=True, null=True)  # Field name made lowercase.
    id_x = models.CharField(db_column='ID_X', max_length=1000, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AppMenuItems'


class Appmenus(models.Model):
    code = models.IntegerField(db_column='Code', primary_key=True)  # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=100, blank=True, null=True)  # Field name made lowercase.
    packages = models.CharField(db_column='Packages', max_length=50, blank=True, null=True)  # Field name made lowercase.
    subpackages = models.CharField(db_column='Subpackages', max_length=50, blank=True, null=True)  # Field name made lowercase.
    displayorder = models.SmallIntegerField(db_column='DisplayOrder', blank=True, null=True)  # Field name made lowercase.
    iconsize = models.SmallIntegerField(db_column='IconSize', blank=True, null=True)  # Field name made lowercase.
    packages_x = models.CharField(db_column='Packages_X', max_length=50, blank=True, null=True)  # Field name made lowercase.
    subpackages_x = models.CharField(db_column='Subpackages_X', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AppMenus'


class Applicationinfo(models.Model):
    code = models.IntegerField(db_column='Code', primary_key=True)  # Field name made lowercase.
    value = models.CharField(db_column='Value', max_length=300, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ApplicationInfo'


class Applicationkey(models.Model):
    serial = models.CharField(max_length=300, blank=True, null=True)
    type = models.CharField(db_column='Type', max_length=50, blank=True, null=True)  # Field name made lowercase.
    register = models.BooleanField(db_column='Register', blank=True, null=True)  # Field name made lowercase.
    clientnum = models.SmallIntegerField(db_column='ClientNum', blank=True, null=True)  # Field name made lowercase.
    support = models.BooleanField(db_column='Support', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ApplicationKey'


class Assignmentdetail(models.Model):
    code = models.IntegerField(db_column='Code', primary_key=True)  # Field name made lowercase. The composite primary key (Code, AssignmentCode) found, that is not supported. The first column is selected.
    assignmentcode = models.IntegerField(db_column='AssignmentCode')  # Field name made lowercase.
    goodcode = models.IntegerField(db_column='GoodCode', blank=True, null=True)  # Field name made lowercase.
    amount = models.DecimalField(db_column='Amount', max_digits=23, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    amount2 = models.DecimalField(db_column='Amount2', max_digits=23, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    cost = models.DecimalField(db_column='Cost', max_digits=23, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    storecode = models.IntegerField(db_column='StoreCode', blank=True, null=True)  # Field name made lowercase.
    comment = models.CharField(db_column='Comment', max_length=500, blank=True, null=True)  # Field name made lowercase.
    width = models.DecimalField(db_column='Width', max_digits=23, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    height = models.DecimalField(db_column='Height', max_digits=23, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    num = models.DecimalField(db_column='Num', max_digits=23, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    global_field = models.ForeignKey('GlobalIds', on_delete=models.DO_NOTHING, db_column='Global_ID', blank=True, null=True)  # Field name made lowercase. Field renamed because it was a Python reserved word.

    class Meta:
        managed = False
        db_table = 'AssignmentDetail'
        unique_together = (('code', 'assignmentcode'),)


class Assignmentgood(models.Model):
    code = models.IntegerField(db_column='Code', primary_key=True)  # Field name made lowercase.
    detail = models.IntegerField(db_column='Detail', blank=True, null=True)  # Field name made lowercase.
    acctype = models.SmallIntegerField(db_column='AccType', blank=True, null=True)  # Field name made lowercase.
    date = models.CharField(db_column='Date', max_length=10, blank=True, null=True)  # Field name made lowercase.
    lastprintdate = models.CharField(db_column='LastPrintDate', max_length=10, blank=True, null=True)  # Field name made lowercase.
    vouchercode = models.IntegerField(db_column='VoucherCode', blank=True, null=True)  # Field name made lowercase.
    sumcost = models.DecimalField(db_column='SumCost', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    comment = models.CharField(db_column='Comment', max_length=500, blank=True, null=True)  # Field name made lowercase.
    interfacename = models.CharField(db_column='InterfaceName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    isautomatic = models.BooleanField(db_column='IsAutomatic', blank=True, null=True)  # Field name made lowercase.
    total = models.IntegerField(db_column='Total', blank=True, null=True)  # Field name made lowercase.
    assistant = models.IntegerField(db_column='Assistant', blank=True, null=True)  # Field name made lowercase.
    expensecenter = models.IntegerField(db_column='ExpenseCenter', blank=True, null=True)  # Field name made lowercase.
    createdtime = models.CharField(db_column='CreatedTime', max_length=5, blank=True, null=True)  # Field name made lowercase.
    createddate = models.CharField(db_column='CreatedDate', max_length=10, blank=True, null=True)  # Field name made lowercase.
    modifiedtime = models.CharField(db_column='ModifiedTime', max_length=5, blank=True, null=True)  # Field name made lowercase.
    modifieddate = models.CharField(db_column='ModifiedDate', max_length=10, blank=True, null=True)  # Field name made lowercase.
    usercreated = models.IntegerField(db_column='UserCreated')  # Field name made lowercase.
    usermodified = models.IntegerField(db_column='UserModified', blank=True, null=True)  # Field name made lowercase.
    owner = models.IntegerField(db_column='Owner')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AssignmentGood'


class Assignmentrelation(models.Model):
    code = models.IntegerField(db_column='Code', primary_key=True)  # Field name made lowercase.
    operationcode = models.IntegerField(db_column='OperationCode', blank=True, null=True)  # Field name made lowercase.
    operationtype = models.SmallIntegerField(db_column='OperationType', blank=True, null=True)  # Field name made lowercase.
    assignmentcode = models.ForeignKey(Assignmentgood, on_delete=models.DO_NOTHING, db_column='AssignmentCode', blank=True, null=True)  # Field name made lowercase.
    groupcode = models.IntegerField(db_column='GroupCode', blank=True, null=True)  # Field name made lowercase.
    groupstatus = models.BooleanField(db_column='GroupStatus', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AssignmentRelation'


class Assignmentsettlement(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True, db_comment='کليد اصلي جدول')  # Field name made lowercase.
    code = models.IntegerField(db_column='Code', unique=True, db_comment='کد')  # Field name made lowercase.
    date = models.CharField(db_column='Date', max_length=10, db_comment='تاريخ')  # Field name made lowercase.
    vouchercode = models.IntegerField(db_column='VoucherCode', blank=True, null=True, db_comment='کد سند حسابداري')  # Field name made lowercase.
    createdtime = models.CharField(db_column='CreatedTime', max_length=5, db_comment='زمان ايجاد')  # Field name made lowercase.
    createddate = models.CharField(db_column='CreatedDate', max_length=10, db_comment='تاريخ ايجاد')  # Field name made lowercase.
    modifiedtime = models.CharField(db_column='ModifiedTime', max_length=5, blank=True, null=True, db_comment='زمان تغيير')  # Field name made lowercase.
    modifieddate = models.CharField(db_column='ModifiedDate', max_length=10, blank=True, null=True, db_comment='تاريخ تغيير')  # Field name made lowercase.
    usercreated = models.IntegerField(db_column='UserCreated', db_comment='کاربر ايجاد کننده')  # Field name made lowercase.
    usermodified = models.IntegerField(db_column='UserModified', blank=True, null=True, db_comment='کاربر تغيير دهنده')  # Field name made lowercase.
    global_id = models.IntegerField(db_column='Global_ID')  # Field name made lowercase.
    comment = models.CharField(db_column='Comment', max_length=500, blank=True, null=True, db_comment='شرح')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AssignmentSettlement'


class Assignmentsettlementdetails(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True, db_comment='کليد اصلي جدول')  # Field name made lowercase. The composite primary key (ID, IsTemp) found, that is not supported. The first column is selected.
    assignmentsettlementid = models.ForeignKey(Assignmentsettlement, on_delete=models.DO_NOTHING, db_column='AssignmentSettlementID', blank=True, null=True, db_comment='کليد فرعي جدول')  # Field name made lowercase.
    assignment_recieveid = models.ForeignKey('AssignmentRecieve', on_delete=models.DO_NOTHING, db_column='Assignment_RecieveID', db_comment='کد حواله حساب')  # Field name made lowercase.
    istemp = models.BooleanField(db_column='IsTemp', db_comment='موقت/اصلي')  # Field name made lowercase.
    com_index = models.IntegerField(db_column='Com_Index')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AssignmentSettlementDetails'
        unique_together = (('id', 'istemp'),)


class AssignmentPay(models.Model):
    id = models.IntegerField(db_column='ID',primary_key=True)  # Field name made lowercase.
    assignmentdate = models.CharField(db_column='AssignmentDate', max_length=10, blank=True, null=True)  # Field name made lowercase.
    assignmentnum = models.CharField(db_column='AssignmentNum', max_length=30, blank=True, null=True)  # Field name made lowercase.
    cost = models.DecimalField(db_column='Cost', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=200, blank=True, null=True)  # Field name made lowercase.
    entitycode = models.IntegerField(db_column='EntityCode', blank=True, null=True)  # Field name made lowercase.
    entitytype = models.BooleanField(db_column='EntityType', blank=True, null=True)  # Field name made lowercase.
    bankname = models.CharField(db_column='BankName', max_length=30, blank=True, null=True)  # Field name made lowercase.
    bankbranch = models.CharField(db_column='BankBranch', max_length=30, blank=True, null=True)  # Field name made lowercase.
    accountid = models.CharField(db_column='AccountID', max_length=30, blank=True, null=True)  # Field name made lowercase.
    sanadcode = models.IntegerField(db_column='SanadCode', blank=True, null=True)  # Field name made lowercase.
    currcode = models.IntegerField(db_column='CurrCode', blank=True, null=True)  # Field name made lowercase.
    currrate = models.DecimalField(db_column='CurrRate', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    bankwagecode = models.IntegerField(db_column='BankWageCode', blank=True, null=True)  # Field name made lowercase.
    bankwagecost = models.DecimalField(db_column='BankWageCost', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Assignment_Pay'


class AssignmentRecieve(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    assignmentdate = models.CharField(db_column='AssignmentDate', max_length=10, blank=True, null=True)  # Field name made lowercase.
    assignmentnum = models.CharField(db_column='AssignmentNum', max_length=50, blank=True, null=True)  # Field name made lowercase.
    cost = models.DecimalField(db_column='Cost', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=200, blank=True, null=True)  # Field name made lowercase.
    bankcode = models.IntegerField(db_column='BankCode', blank=True, null=True)  # Field name made lowercase.
    sanadcode = models.IntegerField(db_column='SanadCode', blank=True, null=True)  # Field name made lowercase.
    flag = models.SmallIntegerField(blank=True, null=True)
    currcode = models.IntegerField(db_column='CurrCode', blank=True, null=True)  # Field name made lowercase.
    currrate = models.DecimalField(db_column='CurrRate', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    assignmenttype = models.SmallIntegerField(db_column='AssignmentType')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Assignment_Recieve'


class Autoanswer(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    state = models.IntegerField(db_column='State', blank=True, null=True)  # Field name made lowercase.
    ring = models.IntegerField(db_column='Ring', blank=True, null=True)  # Field name made lowercase.
    messagepath = models.CharField(db_column='MessagePath', max_length=255, blank=True, null=True)  # Field name made lowercase.
    recordpath = models.CharField(db_column='RecordPath', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AutoAnswer'


class Autobackuphistory(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    actdate = models.CharField(db_column='ActDate', max_length=10, blank=True, null=True)  # Field name made lowercase.
    skipact = models.BooleanField(db_column='SkipAct', blank=True, null=True)  # Field name made lowercase.
    doact = models.BooleanField(db_column='DoAct', blank=True, null=True)  # Field name made lowercase.
    userid = models.IntegerField(db_column='UserID', blank=True, null=True)  # Field name made lowercase.
    backuptype = models.SmallIntegerField(db_column='BackupType', blank=True, null=True)  # Field name made lowercase.
    databasename = models.CharField(db_column='DatabaseName', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AutoBackupHistory'


class Autobackupschedule(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    startdate = models.CharField(db_column='StartDate', max_length=10, blank=True, null=True)  # Field name made lowercase.
    starttime = models.CharField(db_column='StartTime', max_length=5, blank=True, null=True)  # Field name made lowercase.
    levelaction = models.SmallIntegerField(db_column='LevelAction', blank=True, null=True)  # Field name made lowercase.
    periodaction = models.SmallIntegerField(db_column='PeriodAction', blank=True, null=True)  # Field name made lowercase.
    actionactive = models.BooleanField(db_column='ActionActive', blank=True, null=True)  # Field name made lowercase.
    userid = models.IntegerField(db_column='UserID', blank=True, null=True)  # Field name made lowercase.
    savepath = models.CharField(db_column='SavePath', max_length=250, blank=True, null=True)  # Field name made lowercase.
    uploadoncloud = models.BooleanField(db_column='UploadOnCloud', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AutoBackupSchedule'


class Autovouchersetting(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    partcode = models.IntegerField(db_column='PartCode')  # Field name made lowercase.
    typegroup = models.IntegerField(db_column='TypeGroup')  # Field name made lowercase.
    type = models.IntegerField(db_column='Type')  # Field name made lowercase.
    total = models.SmallIntegerField(db_column='Total', blank=True, null=True)  # Field name made lowercase.
    assistant = models.IntegerField(db_column='Assistant', blank=True, null=True)  # Field name made lowercase.
    detail = models.IntegerField(db_column='Detail', blank=True, null=True)  # Field name made lowercase.
    debit = models.CharField(db_column='Debit', max_length=500, blank=True, null=True)  # Field name made lowercase.
    credit = models.CharField(db_column='Credit', max_length=500, blank=True, null=True)  # Field name made lowercase.
    aggregate = models.IntegerField(db_column='Aggregate')  # Field name made lowercase.
    comment = models.CharField(db_column='Comment', max_length=500, blank=True, null=True)  # Field name made lowercase.
    customwhereclause = models.CharField(db_column='CustomWhereClause', max_length=2000, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AutoVoucherSetting'


class Autovouchersettingtemplete(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=50, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=100, blank=True, null=True)  # Field name made lowercase.
    settingfile = models.BinaryField(db_column='SettingFile', blank=True, null=True)  # Field name made lowercase.
    isdefault = models.BooleanField(db_column='IsDefault', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AutoVoucherSettingTemplete'


class BackfactitemsVisitor(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True) # <<< این قسمت اضافه شده
    backfact_code = models.IntegerField(db_column='BackFact_code', blank=True, null=True)  # Field name made lowercase.
    radif = models.IntegerField(db_column='Radif', blank=True, null=True)  # Field name made lowercase.
    good_code = models.IntegerField(db_column='Good_Code', blank=True, null=True)  # Field name made lowercase.
    vis_code = models.IntegerField(db_column='Vis_Code', blank=True, null=True)  # Field name made lowercase.
    vis_percent = models.DecimalField(db_column='Vis_Percent', max_digits=23, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    vis_price = models.DecimalField(db_column='Vis_Price', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    vis_type_pay = models.BooleanField(db_column='Vis_Type_Pay', blank=True, null=True)  # Field name made lowercase.
    tmp = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'BackFactItems_Visitor'


class BackfactDetail(models.Model):
    code = models.IntegerField(primary_key=True)  # The composite primary key (code, radif, type, tmp) found, that is not supported. The first column is selected.
    radif = models.SmallIntegerField()
    type = models.SmallIntegerField()
    tmp = models.SmallIntegerField()
    kala_code = models.IntegerField(blank=True, null=True)
    meghdar = models.DecimalField(max_digits=23, decimal_places=8, blank=True, null=True)
    naghdi = models.DecimalField(max_digits=23, decimal_places=9, blank=True, null=True)
    status = models.SmallIntegerField(blank=True, null=True)
    sanad_code = models.IntegerField(blank=True, null=True)
    meghdar2 = models.DecimalField(max_digits=23, decimal_places=8, blank=True, null=True)
    an_code = models.SmallIntegerField(blank=True, null=True)
    sanad_radif = models.IntegerField(blank=True, null=True)
    sharh = models.CharField(max_length=500, blank=True, null=True)
    com_index = models.IntegerField(db_column='Com_Index')  # Field name made lowercase.
    sanad_type = models.SmallIntegerField(db_column='Sanad_Type')  # Field name made lowercase.
    miangin = models.DecimalField(db_column='Miangin', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    chargepercent = models.DecimalField(db_column='ChargePercent', max_digits=23, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    taxpercent = models.DecimalField(db_column='TaxPercent', max_digits=23, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    currcode = models.IntegerField(db_column='CurrCode', blank=True, null=True)  # Field name made lowercase.
    currrate = models.DecimalField(db_column='CurrRate', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    invoicereturnitemstype = models.SmallIntegerField(db_column='InvoiceReturnItemsType')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BackFact_Detail'
        unique_together = (('code', 'radif', 'type', 'tmp'),)


class Backforosh(models.Model):
    code = models.IntegerField(primary_key=True)  # The composite primary key (code, type, tmp) found, that is not supported. The first column is selected.
    type = models.SmallIntegerField()
    tmp = models.SmallIntegerField()
    shakhs_code = models.IntegerField(blank=True, null=True)
    tarikh = models.CharField(max_length=50, blank=True, null=True)
    sharh = models.CharField(max_length=500, blank=True, null=True)
    status = models.SmallIntegerField(blank=True, null=True)
    takhfif = models.DecimalField(db_column='Takhfif', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    mabvisitor = models.DecimalField(db_column='MabVisitor', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    visitorcode = models.ForeignKey('Perinf', on_delete=models.DO_NOTHING, db_column='visitorCode', blank=True, null=True)  # Field name made lowercase.
    vouchercode = models.IntegerField(db_column='VoucherCode', blank=True, null=True)  # Field name made lowercase.
    expcentercode = models.IntegerField(db_column='ExpCenterCode', blank=True, null=True)  # Field name made lowercase.
    refrenceid = models.CharField(db_column='RefrenceID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    global_field = models.ForeignKey('GlobalIds', on_delete=models.DO_NOTHING, db_column='Global_ID', blank=True, null=True)  # Field name made lowercase. Field renamed because it was a Python reserved word.
    createdtime = models.CharField(db_column='CreatedTime', max_length=5, blank=True, null=True)  # Field name made lowercase.
    createddate = models.CharField(db_column='CreatedDate', max_length=10, blank=True, null=True)  # Field name made lowercase.
    modifiedtime = models.CharField(db_column='ModifiedTime', max_length=5, blank=True, null=True)  # Field name made lowercase.
    modifieddate = models.CharField(db_column='ModifiedDate', max_length=10, blank=True, null=True)  # Field name made lowercase.
    usercreated = models.IntegerField(db_column='UserCreated')  # Field name made lowercase.
    usermodified = models.IntegerField(db_column='UserModified', blank=True, null=True)  # Field name made lowercase.
    takhfif_type = models.BooleanField(db_column='Takhfif_Type', blank=True, null=True)  # Field name made lowercase.
    takhfif_percent = models.DecimalField(db_column='Takhfif_Percent', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    sanad_code = models.IntegerField(blank=True, null=True)
    returnreasonid = models.IntegerField(db_column='ReturnReasonID', blank=True, null=True)  # Field name made lowercase.
    currcode = models.IntegerField(db_column='CurrCode', blank=True, null=True)  # Field name made lowercase.
    currrate = models.DecimalField(db_column='CurrRate', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    owner = models.IntegerField(db_column='Owner')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BackForosh'
        unique_together = (('code', 'type', 'tmp'),)


class Backupfilesonserverlog(models.Model):
    id = id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    createdate = models.CharField(db_column='CreateDate', max_length=10, blank=True, null=True)  # Field name made lowercase.
    createtime = models.CharField(db_column='CreateTime', max_length=8, blank=True, null=True)  # Field name made lowercase.
    appversion = models.CharField(db_column='AppVersion', max_length=15, blank=True, null=True)  # Field name made lowercase.
    filelocation = models.CharField(db_column='FileLocation', max_length=500, blank=True, null=True)  # Field name made lowercase.
    kind = models.SmallIntegerField(db_column='Kind', blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    filesize = models.IntegerField(db_column='FileSize', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BackUpFilesOnServerLog'


class Backupjobschedule(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    active = models.BooleanField(db_column='Active')  # Field name made lowercase.
    startdate = models.DateTimeField(db_column='StartDate')  # Field name made lowercase.
    daysperiod = models.SmallIntegerField(db_column='DaysPeriod')  # Field name made lowercase.
    executetime = models.TimeField(db_column='ExecuteTime')  # Field name made lowercase.
    storagepath = models.CharField(db_column='StoragePath', max_length=1000)  # Field name made lowercase.
    sendtocloud = models.BooleanField(db_column='SendToCloud')  # Field name made lowercase.
    lastsuccessdate = models.DateTimeField(db_column='LastSuccessDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BackupJobSchedule'


class Backupjobscheduleerrorlog(models.Model):
    jobid = models.ForeignKey(Backupjobschedule, on_delete=models.DO_NOTHING, db_column='JobId')  # Field name made lowercase.
    date = models.DateTimeField(db_column='Date')  # Field name made lowercase.
    errormessage = models.TextField(db_column='ErrorMessage', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BackupJobScheduleErrorLog'


class Bank(models.Model):
    code = models.IntegerField(db_column='Code', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=50, blank=True, null=True)  # Field name made lowercase.
    shobe = models.CharField(max_length=50, blank=True, null=True)
    sh_h = models.CharField(max_length=50, blank=True, null=True)
    type = models.CharField(max_length=50, blank=True, null=True)
    mogodi = models.DecimalField(max_digits=23, decimal_places=9, blank=True, null=True)
    tel = models.CharField(db_column='Tel', max_length=50, blank=True, null=True)  # Field name made lowercase.
    fax = models.CharField(db_column='Fax', max_length=50, blank=True, null=True)  # Field name made lowercase.
    comment = models.CharField(db_column='Comment', max_length=500, blank=True, null=True)  # Field name made lowercase.
    code_m = models.ForeignKey('BankM', on_delete=models.DO_NOTHING, db_column='Code_M', blank=True, null=True)  # Field name made lowercase.
    vouchercode = models.IntegerField(db_column='VoucherCode', blank=True, null=True)  # Field name made lowercase.
    firstamount = models.DecimalField(db_column='FirstAmount', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    enddate = models.CharField(db_column='EndDate', max_length=10, blank=True, null=True)  # Field name made lowercase.
    securitycode = models.CharField(db_column='SecurityCode', max_length=4, blank=True, null=True)  # Field name made lowercase.
    cardcode = models.CharField(db_column='CardCode', max_length=16, blank=True, null=True)  # Field name made lowercase.
    shaba = models.CharField(db_column='Shaba', max_length=26, blank=True, null=True)  # Field name made lowercase.
    currcode = models.IntegerField(db_column='CurrCode', blank=True, null=True)  # Field name made lowercase.
    currrate = models.DecimalField(db_column='CurrRate', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    createdtime = models.CharField(db_column='CreatedTime', max_length=5, blank=True, null=True)  # Field name made lowercase.
    createddate = models.CharField(db_column='CreatedDate', max_length=10, blank=True, null=True)  # Field name made lowercase.
    modifiedtime = models.CharField(db_column='ModifiedTime', max_length=5, blank=True, null=True)  # Field name made lowercase.
    modifieddate = models.CharField(db_column='ModifiedDate', max_length=10, blank=True, null=True)  # Field name made lowercase.
    usercreated = models.CharField(db_column='UserCreated', max_length=50, blank=True, null=True)  # Field name made lowercase.
    usermodified = models.CharField(db_column='UserModified', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Bank'


class BankM(models.Model):
    code = models.SmallIntegerField(db_column='Code', primary_key=True)  # Field name made lowercase.
    name = models.CharField(max_length=50, blank=True, null=True)
    comment = models.CharField(db_column='Comment', max_length=500, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Bank_M'


class Banktypes(models.Model):
    typeid = models.AutoField(db_column='TypeId', primary_key=True)  # Field name made lowercase.
    typecode = models.IntegerField(db_column='TypeCode', blank=True, null=True)  # Field name made lowercase.
    typename = models.CharField(db_column='TypeName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    eng_name = models.CharField(db_column='Eng_name', max_length=15, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Banktypes'


class Barcodeformul(models.Model):
    barcodeid = models.IntegerField(db_column='BarCodeID', primary_key=True)  # Field name made lowercase.
    barcodetitle = models.CharField(db_column='BarCodeTitle', max_length=100)  # Field name made lowercase.
    barcodetype = models.SmallIntegerField(db_column='BarCodeType')  # Field name made lowercase.
    digitcount = models.SmallIntegerField(db_column='DigitCount')  # Field name made lowercase.
    constantstart = models.SmallIntegerField(db_column='ConstantStart', blank=True, null=True)  # Field name made lowercase.
    constantcount = models.IntegerField(db_column='ConstantCount', blank=True, null=True)  # Field name made lowercase.
    constantcode = models.CharField(db_column='ConstantCode', max_length=10, blank=True, null=True)  # Field name made lowercase.
    itemcodetype = models.SmallIntegerField(db_column='ItemCodeType', blank=True, null=True)  # Field name made lowercase.
    itemcodestart = models.SmallIntegerField(db_column='ItemCodeStart', blank=True, null=True)  # Field name made lowercase.
    itemcodecount = models.SmallIntegerField(db_column='ItemCodeCount', blank=True, null=True)  # Field name made lowercase.
    itemconstantcode = models.IntegerField(db_column='ItemConstantCode', blank=True, null=True)  # Field name made lowercase.
    pricestart = models.SmallIntegerField(db_column='PriceStart', blank=True, null=True)  # Field name made lowercase.
    pricecount = models.SmallIntegerField(db_column='PriceCount', blank=True, null=True)  # Field name made lowercase.
    amountstart = models.SmallIntegerField(db_column='AmountStart', blank=True, null=True)  # Field name made lowercase.
    amountcount = models.SmallIntegerField(db_column='AmountCount', blank=True, null=True)  # Field name made lowercase.
    amountdivide = models.SmallIntegerField(db_column='AmountDivide', blank=True, null=True)  # Field name made lowercase.
    balancenostart = models.SmallIntegerField(db_column='BalanceNoStart', blank=True, null=True)  # Field name made lowercase.
    balancenocount = models.SmallIntegerField(db_column='BalanceNoCount', blank=True, null=True)  # Field name made lowercase.
    unuseddigitcount = models.SmallIntegerField(db_column='UnUsedDigitCount', blank=True, null=True)  # Field name made lowercase.
    balancenoasstore = models.BooleanField(db_column='BalanceNoAsStore', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BarCodeFormul'


class Bill(models.Model):
    id_check = models.CharField(db_column='ID_CHeck', max_length=50)  # Field name made lowercase.
    date1 = models.CharField(db_column='Date1', max_length=10)  # Field name made lowercase.
    status = models.SmallIntegerField(db_column='Status')  # Field name made lowercase.
    amount = models.DecimalField(db_column='Amount', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    comment = models.CharField(db_column='Comment', max_length=500, blank=True, null=True)  # Field name made lowercase.
    first1 = models.SmallIntegerField(db_column='First1')  # Field name made lowercase.
    id_bank = models.IntegerField(db_column='Id_Bank', blank=True, null=True)  # Field name made lowercase.
    bank = models.CharField(db_column='Bank', max_length=50, blank=True, null=True)  # Field name made lowercase.
    shobe = models.CharField(db_column='Shobe', max_length=50, blank=True, null=True)  # Field name made lowercase.
    id_h = models.CharField(db_column='ID_H', max_length=50, blank=True, null=True)  # Field name made lowercase.
    perid = models.IntegerField(db_column='PerId')  # Field name made lowercase.
    name_rec = models.CharField(db_column='Name_Rec', max_length=50, blank=True, null=True)  # Field name made lowercase.
    lname = models.IntegerField(db_column='LName', blank=True, null=True)  # Field name made lowercase.
    type = models.IntegerField(db_column='Type')  # Field name made lowercase.
    sanad_code = models.IntegerField(db_column='Sanad_Code')  # Field name made lowercase.
    rec = models.IntegerField(db_column='Rec')  # Field name made lowercase.
    operationdate = models.CharField(db_column='OperationDate', max_length=10, blank=True, null=True)  # Field name made lowercase.
    computer_index = models.IntegerField(db_column='Computer_Index')  # Field name made lowercase.
    radif_check = models.IntegerField(db_column='Radif_Check', blank=True, null=True)  # Field name made lowercase.
    date2 = models.CharField(db_column='Date2', max_length=10, blank=True, null=True)  # Field name made lowercase.
    vouchercode = models.IntegerField(db_column='VoucherCode', blank=True, null=True)  # Field name made lowercase.
    paysanadpercode = models.IntegerField(db_column='PaySanadPerCode', blank=True, null=True)  # Field name made lowercase.
    paysanadtype = models.SmallIntegerField(db_column='PaySanadType', blank=True, null=True)  # Field name made lowercase.
    statuscomment = models.CharField(db_column='StatusComment', max_length=500, blank=True, null=True)  # Field name made lowercase.
    location = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Bill'


class CidLinecfg(models.Model):
    lineid = models.SmallIntegerField(db_column='LineID', blank=True, null=True)  # Field name made lowercase.
    public = models.BooleanField(db_column='Public', blank=True, null=True)  # Field name made lowercase.
    ranking = models.BooleanField(db_column='Ranking', blank=True, null=True)  # Field name made lowercase.
    timing = models.BooleanField(db_column='Timing', blank=True, null=True)  # Field name made lowercase.
    interval = models.IntegerField(db_column='Interval', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CID_LineCFG'


class CidQueuecfg(models.Model):
    lineid = models.SmallIntegerField(db_column='LineID', blank=True, null=True)  # Field name made lowercase.
    userip = models.CharField(db_column='UserIP', max_length=15, blank=True, null=True)  # Field name made lowercase.
    username = models.CharField(db_column='UserName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    userstate = models.BooleanField(db_column='UserState', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CID_QueueCFG'


class CidReport(models.Model):
    lineid = models.SmallIntegerField(db_column='LineID', blank=True, null=True)  # Field name made lowercase.
    username = models.CharField(db_column='UserName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    time = models.CharField(db_column='Time', max_length=15, blank=True, null=True)  # Field name made lowercase.
    date = models.CharField(db_column='Date', max_length=15, blank=True, null=True)  # Field name made lowercase.
    state = models.BooleanField(db_column='State', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CID_Report'


class CidSysconfig(models.Model):
    systype = models.SmallIntegerField(db_column='SysType', blank=True, null=True)  # Field name made lowercase.
    host = models.CharField(db_column='Host', max_length=20, blank=True, null=True)  # Field name made lowercase.
    port = models.IntegerField(db_column='Port', blank=True, null=True)  # Field name made lowercase.
    sysstate = models.SmallIntegerField(db_column='SysState', blank=True, null=True)  # Field name made lowercase.
    isserver = models.BooleanField(db_column='IsServer', blank=True, null=True)  # Field name made lowercase.
    systemname = models.CharField(db_column='SystemName', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CID_SysConfig'


class Calcmethod(models.Model):
    code = models.IntegerField(db_column='Code', primary_key=True)  # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=50)  # Field name made lowercase.
    staffins = models.DecimalField(db_column='StaffIns', max_digits=23, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    employerins = models.DecimalField(db_column='EmployerIns', max_digits=23, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    overtime = models.IntegerField(db_column='OverTime')  # Field name made lowercase.
    taxmaincode = models.ForeignKey('Taxmain', on_delete=models.DO_NOTHING, db_column='TaxMainCode', blank=True, null=True)  # Field name made lowercase.
    dailyins = models.DecimalField(db_column='DailyIns', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    dectax = models.BooleanField(db_column='DecTax')  # Field name made lowercase.
    maskok = models.IntegerField(db_column='Maskok')  # Field name made lowercase.
    leaveceil = models.DecimalField(db_column='LeaveCeil', max_digits=23, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    output = models.DecimalField(db_column='OutPut', max_digits=23, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    comment = models.CharField(db_column='Comment', max_length=500, blank=True, null=True)  # Field name made lowercase.
    insurance = models.BooleanField(db_column='Insurance')  # Field name made lowercase.
    tax = models.BooleanField(db_column='Tax')  # Field name made lowercase.
    bedbes = models.BooleanField(db_column='BedBes')  # Field name made lowercase.
    loan = models.BooleanField(db_column='Loan')  # Field name made lowercase.
    overdis = models.BooleanField(db_column='OverDis')  # Field name made lowercase.
    entrance = models.CharField(db_column='Entrance', max_length=5)  # Field name made lowercase.
    exit = models.CharField(db_column='Exit', max_length=5)  # Field name made lowercase.
    leisureins = models.DecimalField(db_column='LeisureIns', max_digits=23, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    dectaxvalue = models.DecimalField(db_column='DecTaxValue', max_digits=23, decimal_places=8, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CalcMethod'


class CalendarEvents(models.Model):
    year = models.CharField(db_column='Year', max_length=4, blank=True, null=True)  # Field name made lowercase.
    monthday = models.CharField(db_column='MonthDay', max_length=5)  # Field name made lowercase.
    holiday = models.BooleanField(db_column='Holiday')  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=500)  # Field name made lowercase.
    id = models.IntegerField(db_column='ID', blank=True, primary_key=True)  # Field name made lowercase.
    syncid = models.BigIntegerField(db_column='SyncID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Calendar_Events'


class Calender(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    date = models.CharField(db_column='Date', unique=True, max_length=10)  # Field name made lowercase.
    day = models.SmallIntegerField(db_column='Day')  # Field name made lowercase.
    type = models.SmallIntegerField(db_column='Type')  # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=30, blank=True, null=True)  # Field name made lowercase.
    comment = models.CharField(db_column='Comment', max_length=500, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Calender'


class Calldata(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    contactname = models.CharField(db_column='ContactName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    contacttelnumber = models.CharField(db_column='ContactTelNumber', max_length=255, blank=True, null=True)  # Field name made lowercase.
    intime = models.CharField(db_column='InTime', max_length=255, blank=True, null=True)  # Field name made lowercase.
    calltime = models.CharField(db_column='CallTime', max_length=255, blank=True, null=True)  # Field name made lowercase.
    answertype = models.CharField(db_column='AnswerType', max_length=255, blank=True, null=True)  # Field name made lowercase.
    voicepath = models.CharField(db_column='VoicePath', max_length=255, blank=True, null=True)  # Field name made lowercase.
    calltype = models.CharField(db_column='CallType', max_length=255, blank=True, null=True)  # Field name made lowercase.
    date = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'CallData'


class Calllist(models.Model):
    srl_calllist = models.AutoField(db_column='Srl_CallList', primary_key=True)  # Field name made lowercase.
    c_customer = models.IntegerField(db_column='C_Customer')  # Field name made lowercase.
    srl_opratorlist = models.IntegerField(db_column='Srl_OpratorList', blank=True, null=True)  # Field name made lowercase.
    n_customer = models.CharField(db_column='N_Customer', max_length=100, blank=True, null=True)  # Field name made lowercase.
    telnumber = models.CharField(db_column='TelNumber', max_length=15)  # Field name made lowercase.
    telline = models.CharField(db_column='TelLine', max_length=15)  # Field name made lowercase.
    d_calllist = models.CharField(db_column='D_CallList', max_length=10)  # Field name made lowercase.
    t_calllist = models.CharField(db_column='T_CallList', max_length=5)  # Field name made lowercase.
    t_endcall = models.CharField(db_column='T_EndCall', max_length=5, blank=True, null=True)  # Field name made lowercase.
    status = models.SmallIntegerField(db_column='Status')  # Field name made lowercase.
    dissaveoprator = models.CharField(db_column='DisSaveOprator', max_length=500, blank=True, null=True)  # Field name made lowercase.
    address_pic = models.CharField(db_column='Address_Pic', max_length=300, blank=True, null=True)  # Field name made lowercase.
    orderanswer = models.IntegerField(db_column='OrderAnswer')  # Field name made lowercase.
    t_startcall = models.CharField(db_column='T_StartCall', max_length=5, blank=True, null=True)  # Field name made lowercase.
    countring = models.IntegerField(db_column='CountRing', blank=True, null=True)  # Field name made lowercase.
    no_calleridmonitor = models.SmallIntegerField(db_column='No_CallerIDMonitor')  # Field name made lowercase.
    timestartcall = models.IntegerField(db_column='TimeStartCall')  # Field name made lowercase.
    servicerowversion = models.BigIntegerField(db_column='ServiceRowVersion')  # Field name made lowercase.
    calleridlineid = models.ForeignKey('Calltelline', on_delete=models.DO_NOTHING, db_column='CallerIdLineID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CallList'


class Calllistdisplay(models.Model):
    srl_calllist = models.IntegerField(db_column='Srl_CallList')  # Field name made lowercase.
    srl_opratorlist = models.IntegerField(db_column='Srl_OpratorList')  # Field name made lowercase.
    valday = models.SmallIntegerField(db_column='ValDay')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CallListDisplay'


class Callopratorgroup(models.Model):
    srl_opratorgroup = models.AutoField(db_column='Srl_OpratorGroup', primary_key=True)  # Field name made lowercase.
    c_opratorgroup = models.IntegerField(db_column='C_OpratorGroup')  # Field name made lowercase.
    n_opratorgroup = models.CharField(db_column='N_OpratorGroup', max_length=50)  # Field name made lowercase.
    is_active = models.BooleanField(db_column='Is_Active')  # Field name made lowercase.
    telline = models.CharField(db_column='TelLine', max_length=15)  # Field name made lowercase.
    orderinlist = models.IntegerField(db_column='OrderInList')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CallOpratorGroup'


class Callopratorgrouptelline(models.Model):
    srl_opratorgroup = models.IntegerField(db_column='Srl_OpratorGroup')  # Field name made lowercase.
    telline = models.CharField(db_column='TelLine', max_length=15)  # Field name made lowercase.
    calleridlineid = models.ForeignKey('Calltelline', on_delete=models.DO_NOTHING, db_column='CallerIdLineID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CallOpratorGroupTelLine'


class Callopratorlisttelline(models.Model):
    srl_opratorlist = models.IntegerField(db_column='Srl_OpratorList')  # Field name made lowercase.
    telline = models.CharField(db_column='TelLine', max_length=15)  # Field name made lowercase.
    calleridlineid = models.ForeignKey('Calltelline', on_delete=models.DO_NOTHING, db_column='CallerIdLineID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CallOpratorListTelLine'


class Calltelline(models.Model):
    srl_telline = models.AutoField(db_column='Srl_TelLine', primary_key=True)  # Field name made lowercase.
    telline = models.CharField(db_column='TelLine', max_length=15, unique=True) # <<< primary_key=True حذف و unique=True اضافه شود
    lineport = models.SmallIntegerField(db_column='LinePort')  # Field name made lowercase.
    deviceid = models.CharField(db_column='DeviceID', max_length=30, blank=True, null=True)  # Field name made lowercase.
    serviceip = models.CharField(db_column='ServiceIP', max_length=30, blank=True, null=True)  # Field name made lowercase.
    softwareid = models.SmallIntegerField(db_column='SoftwareId', blank=True, null=True)  # Field name made lowercase.
    devicetype = models.IntegerField(db_column='DeviceType', blank=True, null=True)  # Field name made lowercase.
    servicerowversion = models.BigIntegerField(db_column='ServiceRowVersion')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CallTelLine'
        unique_together = (('lineport', 'deviceid'),)


class Cashqueue(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    ordercode = models.ForeignKey('Order', on_delete=models.DO_NOTHING, db_column='OrderCode')  # Field name made lowercase.
    enterdate = models.CharField(db_column='EnterDate', max_length=10)  # Field name made lowercase.
    entertime = models.CharField(db_column='EnterTime', max_length=5)  # Field name made lowercase.
    reccode = models.IntegerField(db_column='RecCode', blank=True, null=True)  # Field name made lowercase.
    exittime = models.CharField(db_column='ExitTime', max_length=5, blank=True, null=True)  # Field name made lowercase.
    userid = models.ForeignKey('Users', on_delete=models.DO_NOTHING, db_column='UserId')  # Field name made lowercase.
    exituserid = models.ForeignKey('Users', on_delete=models.DO_NOTHING, db_column='ExitUserId', related_name='cashqueue_exituserid_set', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CashQueue'


class Category(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    desc = models.TextField(db_column='Desc', blank=True, null=True)  # Field name made lowercase.
    create_date = models.CharField(max_length=20, blank=True, null=True)
    modify_date = models.CharField(db_column='Modify_date', max_length=20, blank=True, null=True)  # Field name made lowercase.
    create_user = models.IntegerField(db_column='create_User', blank=True, null=True)  # Field name made lowercase.
    modify_user = models.IntegerField(db_column='Modify_User', blank=True, null=True)  # Field name made lowercase.
    parent_code = models.IntegerField(db_column='Parent_code')  # Field name made lowercase.
    type = models.BooleanField(db_column='Type')  # Field name made lowercase.
    flagin = models.BooleanField(db_column='FlagIN', blank=True, null=True)  # Field name made lowercase.
    level = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Category'


class Chartparts(models.Model):
    code = models.IntegerField(db_column='Code', primary_key=True)  # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=50, blank=True, null=True)  # Field name made lowercase.
    englishtitle = models.CharField(db_column='EnglishTitle', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ChartParts'


class Chartreport(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=50, blank=True, null=True)  # Field name made lowercase.
    caption = models.CharField(db_column='Caption', max_length=50, blank=True, null=True)  # Field name made lowercase.
    query = models.CharField(db_column='Query', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    groupby = models.CharField(db_column='GroupBy', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    fil = models.CharField(db_column='Fil', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    where = models.CharField(db_column='Where', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    flag = models.IntegerField(db_column='Flag', blank=True, null=True)  # Field name made lowercase.
    next = models.ForeignKey('self', on_delete=models.DO_NOTHING, db_column='Next', blank=True, null=True)  # Field name made lowercase.
    date = models.CharField(db_column='Date', max_length=10, blank=True, null=True)  # Field name made lowercase.
    softwarepart = models.ForeignKey('Softwarepart', on_delete=models.DO_NOTHING, db_column='SoftWarePart', blank=True, null=True)  # Field name made lowercase.
    type = models.IntegerField(db_column='Type', blank=True, null=True)  # Field name made lowercase.
    istmp = models.IntegerField(db_column='ISTMP', blank=True, null=True)  # Field name made lowercase.
    clientnumber = models.SmallIntegerField(db_column='ClientNumber', blank=True, null=True)  # Field name made lowercase.
    comment = models.CharField(db_column='Comment', max_length=250, blank=True, null=True)  # Field name made lowercase.
    color = models.CharField(db_column='Color', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ChartReport'


class Chartseries(models.Model):
    code = models.IntegerField(db_column='Code', primary_key=True)  # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=50, blank=True, null=True)  # Field name made lowercase.
    filterstr = models.CharField(db_column='Filterstr', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ChartSeries'


class Chartvaluefields(models.Model):
    code = models.IntegerField(db_column='Code', primary_key=True)  # Field name made lowercase.
    labelfieldscode = models.ForeignKey('Chartlabelfields', on_delete=models.DO_NOTHING, db_column='LabelFieldsCode', blank=True, null=True)  # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=50, blank=True, null=True)  # Field name made lowercase.
    englishtitle = models.CharField(db_column='EnglishTitle', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ChartValueFields'


class Chartlabelfields(models.Model):
    code = models.IntegerField(db_column='Code', primary_key=True)  # Field name made lowercase.
    partcode = models.ForeignKey(Chartparts, on_delete=models.DO_NOTHING, db_column='PartCode', blank=True, null=True)  # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=50, blank=True, null=True)  # Field name made lowercase.
    englishtitle = models.CharField(db_column='EnglishTitle', max_length=50, blank=True, null=True)  # Field name made lowercase.
    datatype = models.CharField(db_column='DataType', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ChartlabelFields'


class Checkband(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    bankcode = models.ForeignKey(Bank, on_delete=models.DO_NOTHING, db_column='BankCode')  # Field name made lowercase.
    date = models.CharField(db_column='Date', max_length=10)  # Field name made lowercase.
    serial = models.CharField(db_column='Serial', max_length=10)  # Field name made lowercase.
    fromnum = models.CharField(db_column='FromNum', max_length=50)  # Field name made lowercase.
    tonum = models.CharField(db_column='ToNum', max_length=50)  # Field name made lowercase.
    comment = models.CharField(db_column='Comment', max_length=500, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CheckBand'


class Checkbandsize(models.Model):
    code = models.IntegerField(db_column='Code', primary_key=True)  # Field name made lowercase.
    checktitle = models.CharField(db_column='CheckTitle', max_length=50)  # Field name made lowercase.
    datenumtop = models.IntegerField(db_column='DateNumTop', blank=True, null=True)  # Field name made lowercase.
    datenumleft = models.IntegerField(db_column='DateNumLeft', blank=True, null=True)  # Field name made lowercase.
    datetop = models.IntegerField(db_column='DateTop', blank=True, null=True)  # Field name made lowercase.
    dateleft = models.IntegerField(db_column='DateLeft', blank=True, null=True)  # Field name made lowercase.
    costwordtop = models.IntegerField(db_column='CostWordTop', blank=True, null=True)  # Field name made lowercase.
    costwordleft = models.IntegerField(db_column='CostWordLeft', blank=True, null=True)  # Field name made lowercase.
    paytotop = models.IntegerField(db_column='PaytoTop', blank=True, null=True)  # Field name made lowercase.
    paytoleft = models.IntegerField(db_column='PaytoLeft', blank=True, null=True)  # Field name made lowercase.
    costtop = models.IntegerField(db_column='CostTop', blank=True, null=True)  # Field name made lowercase.
    costleft = models.IntegerField(db_column='CostLeft', blank=True, null=True)  # Field name made lowercase.
    perferazhtop = models.IntegerField(db_column='PerferazhTop', blank=True, null=True)  # Field name made lowercase.
    perferazhleft = models.IntegerField(db_column='PerferazhLeft', blank=True, null=True)  # Field name made lowercase.
    costwidthword = models.IntegerField(db_column='CostWidthWord', blank=True, null=True)  # Field name made lowercase.
    paytowidth = models.IntegerField(db_column='PaytoWidth', blank=True, null=True)  # Field name made lowercase.
    costwidth = models.IntegerField(db_column='CostWidth', blank=True, null=True)  # Field name made lowercase.
    sheetwidth = models.IntegerField(db_column='SheetWidth', blank=True, null=True)  # Field name made lowercase.
    sheetlength = models.IntegerField(db_column='SheetLength', blank=True, null=True)  # Field name made lowercase.
    isdefault = models.BooleanField(db_column='IsDefault', blank=True, null=True)  # Field name made lowercase.
    withoutwritebacktop = models.IntegerField(db_column='WithoutWriteBackTop', blank=True, null=True)  # Field name made lowercase.
    withoutwritebackleft = models.IntegerField(db_column='WithoutWriteBackLeft', blank=True, null=True)  # Field name made lowercase.
    nationalcodetop = models.IntegerField(db_column='NationalCodeTop', blank=True, null=True)  # Field name made lowercase.
    nationalcodeleft = models.IntegerField(db_column='NationalCodeLeft', blank=True, null=True)  # Field name made lowercase.
    nationalcodewidth = models.IntegerField(db_column='NationalCodeWidth', blank=True, null=True)  # Field name made lowercase.
    checktype = models.IntegerField(db_column='CheckType', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CheckBandSize'


class Checkincheckout(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    staffcode = models.ForeignKey('Staff', on_delete=models.DO_NOTHING, db_column='StaffCode')  # Field name made lowercase.
    entrancedate = models.CharField(db_column='EntranceDate', max_length=10)  # Field name made lowercase.
    entrancetime = models.CharField(db_column='EntranceTime', max_length=5, blank=True, null=True)  # Field name made lowercase.
    exitdate = models.CharField(db_column='ExitDate', max_length=10, blank=True, null=True)  # Field name made lowercase.
    exittime = models.CharField(db_column='ExitTime', max_length=5, blank=True, null=True)  # Field name made lowercase.
    type = models.SmallIntegerField(db_column='Type')  # Field name made lowercase.
    type2 = models.SmallIntegerField(db_column='Type2', blank=True, null=True)  # Field name made lowercase.
    type3 = models.SmallIntegerField(db_column='Type3', blank=True, null=True)  # Field name made lowercase.
    comment = models.CharField(db_column='Comment', max_length=500, blank=True, null=True)  # Field name made lowercase.
    exit = models.DateTimeField(db_column='Exit', blank=True, null=True)  # Field name made lowercase.
    entrance = models.DateTimeField(db_column='Entrance', blank=True, null=True)  # Field name made lowercase.
    exittimecheck = models.BooleanField(db_column='ExitTimeCheck', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CheckInCheckOut'


class ChequepayLog(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    chequepayid = models.ForeignKey('ChequePay', on_delete=models.DO_NOTHING, db_column='ChequePAyID', blank=True, null=True)  # Field name made lowercase.
    status = models.IntegerField(db_column='Status', blank=True, null=True)  # Field name made lowercase.
    operationcode = models.IntegerField(db_column='OperationCode', blank=True, null=True)  # Field name made lowercase.
    operationtype = models.SmallIntegerField(db_column='OperationType', blank=True, null=True)  # Field name made lowercase.
    vouchercode = models.IntegerField(db_column='VoucherCode', blank=True, null=True)  # Field name made lowercase.
    entitycode = models.IntegerField(db_column='EntityCode', blank=True, null=True)  # Field name made lowercase.
    date = models.CharField(db_column='Date', max_length=10, blank=True, null=True)  # Field name made lowercase.
    location = models.CharField(db_column='Location', max_length=50, blank=True, null=True)  # Field name made lowercase.
    locationcomment = models.CharField(db_column='LocationComment', max_length=500, blank=True, null=True)  # Field name made lowercase.
    expcentercode = models.IntegerField(db_column='ExpCenterCode', blank=True, null=True)  # Field name made lowercase.
    usercreated = models.IntegerField(db_column='UserCreated')  # Field name made lowercase.
    createdtime = models.CharField(db_column='CreatedTime', max_length=5)  # Field name made lowercase.
    createddate = models.CharField(db_column='CreatedDate', max_length=10)  # Field name made lowercase.
    modifiedtime = models.CharField(db_column='ModifiedTime', max_length=5, blank=True, null=True)  # Field name made lowercase.
    modifieddate = models.CharField(db_column='ModifiedDate', max_length=10, blank=True, null=True)  # Field name made lowercase.
    usermodified = models.IntegerField(db_column='UserModified', blank=True, null=True)  # Field name made lowercase.
    owner = models.IntegerField(db_column='Owner')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ChequePay_Log'


class Chequerecievelog(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    chequerecieveid = models.ForeignKey('ChequesRecieve', on_delete=models.DO_NOTHING, db_column='ChequeRecieveID')  # Field name made lowercase.
    status = models.SmallIntegerField(db_column='Status')  # Field name made lowercase.
    operationcode = models.IntegerField(db_column='OperationCode', blank=True, null=True)  # Field name made lowercase.
    vouchercode = models.IntegerField(db_column='VoucherCode', blank=True, null=True)  # Field name made lowercase.
    entitycode = models.IntegerField(db_column='EntityCode', blank=True, null=True)  # Field name made lowercase.
    date = models.CharField(db_column='Date', max_length=10, blank=True, null=True)  # Field name made lowercase.
    location = models.CharField(db_column='Location', max_length=30, blank=True, null=True)  # Field name made lowercase.
    locationcomment = models.CharField(db_column='LocationComment', max_length=500, blank=True, null=True)  # Field name made lowercase.
    operationtype = models.SmallIntegerField(db_column='OperationType', blank=True, null=True)  # Field name made lowercase.
    expcentercode = models.IntegerField(db_column='ExpCenterCode', blank=True, null=True)  # Field name made lowercase.
    usercreated = models.IntegerField(db_column='UserCreated')  # Field name made lowercase.
    createdtime = models.CharField(db_column='CreatedTime', max_length=5)  # Field name made lowercase.
    createddate = models.CharField(db_column='CreatedDate', max_length=10)  # Field name made lowercase.
    modifiedtime = models.CharField(db_column='ModifiedTime', max_length=5, blank=True, null=True)  # Field name made lowercase.
    modifieddate = models.CharField(db_column='ModifiedDate', max_length=10, blank=True, null=True)  # Field name made lowercase.
    usermodified = models.IntegerField(db_column='UserModified', blank=True, null=True)  # Field name made lowercase.
    owner = models.IntegerField(db_column='Owner')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ChequeRecieveLog'


class ChequePay(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    chequeid = models.CharField(db_column='ChequeID', max_length=30, blank=True, null=True)  # Field name made lowercase.
    chequerow = models.IntegerField(db_column='ChequeRow', blank=True, null=True)  # Field name made lowercase.
    issuancedate = models.CharField(db_column='IssuanceDate', max_length=10, blank=True, null=True)  # Field name made lowercase.
    chequedate = models.CharField(db_column='ChequeDate', max_length=10, blank=True, null=True)  # Field name made lowercase.
    cost = models.DecimalField(db_column='Cost', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    bankcode = models.IntegerField(db_column='BankCode', blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=200, blank=True, null=True)  # Field name made lowercase.
    status = models.IntegerField(blank=True, null=True)
    firstperiod = models.BooleanField(db_column='FirstPeriod', blank=True, null=True)  # Field name made lowercase.
    chequeidcounter = models.IntegerField(db_column='ChequeIDCounter', blank=True, null=True)  # Field name made lowercase.
    percode = models.IntegerField(db_column='PerCode', blank=True, null=True)  # Field name made lowercase.
    recievestatus = models.IntegerField(db_column='RecieveStatus', blank=True, null=True)  # Field name made lowercase.
    currcode = models.IntegerField(db_column='CurrCode', blank=True, null=True)  # Field name made lowercase.
    currrate = models.DecimalField(db_column='CurrRate', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    usercreated = models.IntegerField(db_column='UserCreated')  # Field name made lowercase.
    createdtime = models.CharField(db_column='CreatedTime', max_length=5)  # Field name made lowercase.
    createddate = models.CharField(db_column='CreatedDate', max_length=10)  # Field name made lowercase.
    modifiedtime = models.CharField(db_column='ModifiedTime', max_length=5, blank=True, null=True)  # Field name made lowercase.
    modifieddate = models.CharField(db_column='ModifiedDate', max_length=10, blank=True, null=True)  # Field name made lowercase.
    usermodified = models.IntegerField(db_column='UserModified', blank=True, null=True)  # Field name made lowercase.
    owner = models.IntegerField(db_column='Owner')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Cheque_Pay'
        unique_together = (('chequeid', 'chequeidcounter'),)


class ChequesRecieve(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    chequeid = models.CharField(db_column='ChequeID', max_length=30)  # Field name made lowercase.
    chequerow = models.IntegerField(db_column='CHequeRow', blank=True, null=True)  # Field name made lowercase.
    issuancedate = models.CharField(db_column='IssuanceDate', max_length=10, blank=True, null=True)  # Field name made lowercase.
    chequedate = models.CharField(db_column='ChequeDate', max_length=10, blank=True, null=True)  # Field name made lowercase.
    cost = models.DecimalField(db_column='Cost', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    bankname = models.CharField(db_column='BankName', max_length=50)  # Field name made lowercase.
    bankbranch = models.CharField(db_column='BankBranch', max_length=50, blank=True, null=True)  # Field name made lowercase.
    accountid = models.CharField(db_column='AccountID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=200, blank=True, null=True)  # Field name made lowercase.
    status = models.SmallIntegerField(db_column='Status')  # Field name made lowercase.
    percode = models.IntegerField(db_column='PerCode', blank=True, null=True)  # Field name made lowercase.
    firstperiod = models.BooleanField(db_column='FirstPeriod', blank=True, null=True)  # Field name made lowercase.
    chequeidcounter = models.SmallIntegerField(db_column='ChequeIDCounter', blank=True, null=True)  # Field name made lowercase.
    currcode = models.IntegerField(db_column='CurrCode', blank=True, null=True)  # Field name made lowercase.
    currrate = models.DecimalField(db_column='CurrRate', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    iban = models.CharField(db_column='IBAN', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sayadid = models.CharField(db_column='SayadId', max_length=50, blank=True, null=True)  # Field name made lowercase.
    usercreated = models.IntegerField(db_column='UserCreated')  # Field name made lowercase.
    createdtime = models.CharField(db_column='CreatedTime', max_length=5)  # Field name made lowercase.
    createddate = models.CharField(db_column='CreatedDate', max_length=10)  # Field name made lowercase.
    modifiedtime = models.CharField(db_column='ModifiedTime', max_length=5, blank=True, null=True)  # Field name made lowercase.
    modifieddate = models.CharField(db_column='ModifiedDate', max_length=10, blank=True, null=True)  # Field name made lowercase.
    usermodified = models.IntegerField(db_column='UserModified', blank=True, null=True)  # Field name made lowercase.
    owner = models.IntegerField(db_column='Owner')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Cheques_Recieve'
        unique_together = (('chequeid', 'chequeidcounter'),)


class Cleartables(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    tablename = models.CharField(db_column='TABLEName', max_length=50)  # Field name made lowercase.
    clrdb_condition = models.CharField(db_column='CLRDB_Condition', max_length=200, blank=True, null=True)  # Field name made lowercase.
    fy_condition = models.CharField(db_column='FY_Condition', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    cleardb = models.BooleanField(db_column='ClearDB', blank=True, null=True)  # Field name made lowercase.
    fiscalyear = models.BooleanField(db_column='FiscalYear', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ClearTables'


class CodelockTbl(models.Model):
    com_index = models.IntegerField(db_column='Com_Index')  # Field name made lowercase.
    code = models.CharField(db_column='Code', max_length=35, blank=True, null=True)  # Field name made lowercase.
    status = models.IntegerField(db_column='Status', blank=True, null=True)  # Field name made lowercase.
    tmp = models.BooleanField(db_column='Tmp', blank=True, null=True)  # Field name made lowercase.
    parentcode = models.DecimalField(db_column='ParentCode', max_digits=28, decimal_places=0, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CodeLock_TBL'


class Confirmations(models.Model):
    id = models.IntegerField(db_column='ID',primary_key=True)  # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=200)  # Field name made lowercase.
    status = models.SmallIntegerField(db_column='Status')  # Field name made lowercase.
    trackingid = models.CharField(db_column='TrackingID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    submitionid = models.CharField(db_column='SubmitionID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    comment = models.CharField(db_column='Comment', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Confirmations'


class ConfirmationsUsed(models.Model):
    id = models.IntegerField(db_column='ID',primary_key=True)  # Field name made lowercase.
    trackingid = models.CharField(db_column='TrackingID', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Confirmations_Used'


class ConstantprdDetails(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    prdcode = models.IntegerField(db_column='PrdCode')  # Field name made lowercase.
    type = models.SmallIntegerField(db_column='Type')  # Field name made lowercase.
    costcode = models.IntegerField(db_column='CostCode')  # Field name made lowercase.
    store = models.IntegerField(db_column='Store', blank=True, null=True)  # Field name made lowercase.
    amount = models.DecimalField(db_column='Amount', max_digits=23, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    amount2 = models.DecimalField(db_column='Amount2', max_digits=23, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    cost = models.DecimalField(db_column='Cost', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    comment = models.CharField(db_column='Comment', max_length=500, blank=True, null=True)  # Field name made lowercase.
    tmp = models.SmallIntegerField()
    rowid = models.IntegerField(db_column='RowId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ConstantPrd_Details'


class ConstantprdFormuladetails(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    prdcode = models.IntegerField(db_column='PrdCode')  # Field name made lowercase.
    type = models.SmallIntegerField(db_column='Type')  # Field name made lowercase.
    costcode = models.IntegerField(db_column='CostCode')  # Field name made lowercase.
    amount = models.DecimalField(db_column='Amount', max_digits=23, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    cost = models.DecimalField(db_column='Cost', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    comment = models.CharField(db_column='Comment', max_length=500, blank=True, null=True)  # Field name made lowercase.
    tmp = models.SmallIntegerField()
    amount2 = models.DecimalField(db_column='Amount2', max_digits=23, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    rowid = models.IntegerField(db_column='RowId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ConstantPrd_FormulaDetails'


class Constantproduction(models.Model):
    code = models.IntegerField(db_column='Code', primary_key=True)  # Field name made lowercase.
    formula = models.ForeignKey('Produceformula', on_delete=models.DO_NOTHING, db_column='Formula')  # Field name made lowercase.
    amount = models.DecimalField(db_column='Amount', max_digits=23, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    date = models.CharField(db_column='Date', max_length=10, blank=True, null=True)  # Field name made lowercase.
    identifier = models.CharField(db_column='Identifier', max_length=50, blank=True, null=True)  # Field name made lowercase.
    watcher = models.CharField(db_column='Watcher', max_length=200, blank=True, null=True)  # Field name made lowercase.
    goodstore = models.IntegerField(db_column='GoodStore')  # Field name made lowercase.
    productstore = models.IntegerField(db_column='ProductStore')  # Field name made lowercase.
    productcost = models.DecimalField(db_column='ProductCost', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    vouchercode = models.IntegerField(db_column='VoucherCode', blank=True, null=True)  # Field name made lowercase.
    comment = models.CharField(db_column='Comment', max_length=500, blank=True, null=True)  # Field name made lowercase.
    amount2 = models.DecimalField(db_column='Amount2', max_digits=23, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    global_field = models.ForeignKey('GlobalIds', on_delete=models.DO_NOTHING, db_column='Global_ID', blank=True, null=True)  # Field name made lowercase. Field renamed because it was a Python reserved word.
    expcentercode = models.IntegerField(db_column='ExpCenterCode', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ConstantProduction'


class Contact(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    firstname = models.CharField(db_column='FirstName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    lastname = models.CharField(db_column='LastName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=255, blank=True, null=True)  # Field name made lowercase.
    cellnumber = models.CharField(db_column='CellNumber', max_length=50)  # Field name made lowercase.
    telnumber = models.CharField(db_column='TelNumber', max_length=50)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=50, blank=True, null=True)  # Field name made lowercase.
    picture = models.BinaryField(db_column='Picture', blank=True, null=True)  # Field name made lowercase.
    respect = models.CharField(db_column='Respect', max_length=50, blank=True, null=True)  # Field name made lowercase.
    company = models.CharField(db_column='Company', max_length=255, blank=True, null=True)  # Field name made lowercase.
    faxnumber = models.CharField(db_column='FaxNumber', max_length=255, blank=True, null=True)  # Field name made lowercase.
    referrals = models.CharField(db_column='Referrals', max_length=255, blank=True, null=True)  # Field name made lowercase.
    otelnumber = models.CharField(db_column='OTelNumber', max_length=255, blank=True, null=True)  # Field name made lowercase.
    description = models.TextField(db_column='Description', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Contact'


class Contactmahak(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    contentid = models.IntegerField(db_column='ContentID')  # Field name made lowercase.
    createuserid = models.IntegerField(db_column='CreateUserID')  # Field name made lowercase.
    createtime = models.CharField(db_column='CreateTime', max_length=20)  # Field name made lowercase.
    content = models.CharField(db_column='Content', max_length=1000)  # Field name made lowercase.
    contenttype = models.CharField(db_column='ContentType', max_length=100)  # Field name made lowercase.
    fullname = models.CharField(db_column='FullName', max_length=200)  # Field name made lowercase.
    tellno = models.CharField(db_column='TellNO', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ContactMahak'


class Contactus(models.Model):
    code = models.IntegerField(db_column='Code', primary_key=True)  # Field name made lowercase.
    agenttypeid = models.IntegerField(db_column='AgentTypeID')  # Field name made lowercase.
    agenttypename = models.CharField(db_column='AgentTypeName', max_length=200, blank=True, null=True)  # Field name made lowercase.
    stateid = models.IntegerField(db_column='StateID')  # Field name made lowercase.
    statename = models.CharField(db_column='StateName', max_length=200, blank=True, null=True)  # Field name made lowercase.
    cityid = models.IntegerField(db_column='CityID')  # Field name made lowercase.
    cityname = models.CharField(db_column='CityName', max_length=250, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=250, blank=True, null=True)  # Field name made lowercase.
    operatorname = models.CharField(db_column='OperatorName', max_length=250, blank=True, null=True)  # Field name made lowercase.
    tel = models.CharField(db_column='Tel', max_length=100, blank=True, null=True)  # Field name made lowercase.
    website = models.CharField(db_column='WebSite', max_length=200, blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=300, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ContactUS'


class Convertcurrencybasetables(models.Model):
    table_schema = models.CharField(db_column='Table_Schema', max_length=100)  # Field name made lowercase.
    table_name = models.CharField(db_column='Table_Name', max_length=100)  # Field name made lowercase.
    sqltext = models.TextField(db_column='SqlText')  # Field name made lowercase.
    sqltextcurrbase = models.TextField(db_column='SqlTextCurrBase', blank=True, null=True)  # Field name made lowercase.
    sqltextcurrnorm = models.TextField(db_column='SqlTextCurrNorm', blank=True, null=True)  # Field name made lowercase.
    noupdatefieldcurrbase = models.CharField(db_column='NoUpdateFieldCurrBase', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    noupdatefieldcurrnorm = models.CharField(db_column='NoUpdateFieldCurrNorm', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    rowcountupdate = models.IntegerField(db_column='RowCountUpdate', blank=True, null=True)  # Field name made lowercase.
    errorexecsql = models.IntegerField(db_column='ErrorExecSql', blank=True, null=True)  # Field name made lowercase.
    desconvert = models.CharField(db_column='DesConvert', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    isconvertcurrency = models.SmallIntegerField(db_column='IsConvertCurrency', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ConvertCurrencyBaseTables'


class Costlevel(models.Model):
    code = models.IntegerField(db_column='Code', primary_key=True)  # Field name made lowercase. The composite primary key (Code, CostType) found, that is not supported. The first column is selected.
    name = models.CharField(db_column='Name', max_length=100, blank=True, null=True)  # Field name made lowercase.
    comment = models.CharField(db_column='Comment', max_length=500, blank=True, null=True)  # Field name made lowercase.
    costtype = models.SmallIntegerField(db_column='CostType')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CostLevel'
        unique_together = (('code', 'costtype'), ('name', 'costtype'),)


class Currencyconversionvouchers(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    currcode = models.BigIntegerField(db_column='CurrCode', blank=True, null=True)  # Field name made lowercase.
    currrate = models.DecimalField(db_column='CurrRate', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    conversionlevel = models.SmallIntegerField(db_column='ConversionLevel', blank=True, null=True)  # Field name made lowercase.
    enddate = models.CharField(db_column='EndDate', max_length=10, blank=True, null=True)  # Field name made lowercase.
    vouchercode = models.BigIntegerField(db_column='VoucherCode', blank=True, null=True)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate', blank=True, null=True)  # Field name made lowercase.
    modifieddate = models.DateTimeField(db_column='ModifiedDate', blank=True, null=True)  # Field name made lowercase.
    usercreated = models.CharField(db_column='UserCreated', max_length=100, blank=True, null=True)  # Field name made lowercase.
    usermodified = models.CharField(db_column='UserModified', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CurrencyConversionVouchers'


class Databaseupdater(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    code = models.IntegerField(db_column='Code', unique=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=100)  # Field name made lowercase.
    value = models.CharField(db_column='Value', max_length=1024)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DatabaseUpdater'


class Deduction(models.Model):
    code = models.IntegerField(db_column='Code', primary_key=True)  # Field name made lowercase.
    title = models.CharField(db_column='Title', unique=True, max_length=50)  # Field name made lowercase.
    cost = models.DecimalField(db_column='Cost', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    comment = models.CharField(db_column='Comment', max_length=500, blank=True, null=True)  # Field name made lowercase.
    calctype = models.SmallIntegerField(db_column='CalcType')  # Field name made lowercase.
    grpcode = models.ForeignKey('Deductiongrp', on_delete=models.DO_NOTHING, db_column='GrpCode')  # Field name made lowercase.
    kol = models.SmallIntegerField(db_column='Kol', blank=True, null=True)  # Field name made lowercase.
    moin = models.SmallIntegerField(db_column='Moin', blank=True, null=True)  # Field name made lowercase.
    tafzili = models.IntegerField(db_column='Tafzili', blank=True, null=True)  # Field name made lowercase.
    usercreated = models.IntegerField(db_column='UserCreated')  # Field name made lowercase.
    createdtime = models.CharField(db_column='CreatedTime', max_length=5)  # Field name made lowercase.
    createddate = models.CharField(db_column='CreatedDate', max_length=10)  # Field name made lowercase.
    modifiedtime = models.CharField(db_column='ModifiedTime', max_length=5, blank=True, null=True)  # Field name made lowercase.
    modifieddate = models.CharField(db_column='ModifiedDate', max_length=10, blank=True, null=True)  # Field name made lowercase.
    usermodified = models.IntegerField(db_column='UserModified', blank=True, null=True)  # Field name made lowercase.
    owner = models.IntegerField(db_column='Owner')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Deduction'


class Deductiongrp(models.Model):
    code = models.IntegerField(db_column='Code', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', unique=True, max_length=50)  # Field name made lowercase.
    comment = models.CharField(db_column='Comment', max_length=500, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DeductionGrp'


class Defaultusercategory(models.Model):
    code_category = models.IntegerField(db_column='Code_category')  # Field name made lowercase.
    user_code = models.IntegerField(db_column='User_code')  # Field name made lowercase.
    id = models.AutoField(primary_key=True)
    active = models.BooleanField(blank=True, null=True)
    person = models.BooleanField(blank=True, null=True)
    good = models.BooleanField(db_column='Good', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DefaultUserCategory'


class Depositinf(models.Model):
    id = models.SmallAutoField(primary_key=True)
    checknum = models.CharField(db_column='CheckNum', max_length=20, blank=True, null=True)  # Field name made lowercase.
    accchecknum = models.CharField(db_column='AccCheckNum', max_length=20, blank=True, null=True)  # Field name made lowercase.
    checkdate = models.CharField(db_column='CheckDate', max_length=10, blank=True, null=True)  # Field name made lowercase.
    checkbankname = models.CharField(db_column='CheckBankName', max_length=40, blank=True, null=True)  # Field name made lowercase.
    checkbranchname = models.CharField(db_column='CheckBranchName', max_length=40, blank=True, null=True)  # Field name made lowercase.
    checkcurrency = models.DecimalField(db_column='CheckCurrency', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    branchname = models.CharField(db_column='BranchName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    branchno = models.CharField(db_column='BranchNo', max_length=50, blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=50, blank=True, null=True)  # Field name made lowercase.
    tel = models.CharField(db_column='Tel', max_length=50, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=50, blank=True, null=True)  # Field name made lowercase.
    isprint = models.SmallIntegerField(db_column='isPrint')  # Field name made lowercase.
    dateprint = models.CharField(db_column='DatePrint', max_length=10, blank=True, null=True)  # Field name made lowercase.
    kindaccprint = models.CharField(db_column='KindAccPrint', max_length=50, blank=True, null=True)  # Field name made lowercase.
    accnumprint = models.CharField(db_column='AccNumPrint', max_length=50, blank=True, null=True)  # Field name made lowercase.
    idnoprint = models.CharField(db_column='IDNoPrint', max_length=50, blank=True, null=True)  # Field name made lowercase.
    postcodeprint = models.CharField(db_column='PostCodePrint', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DepositInf'


class Detailtypes(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=100)  # Field name made lowercase.
    detailtype = models.SmallIntegerField(db_column='DetailType')  # Field name made lowercase.
    isrequired = models.BooleanField(db_column='IsRequired')  # Field name made lowercase.
    toggletitletrue = models.CharField(db_column='ToggleTitleTrue', max_length=50, blank=True, null=True)  # Field name made lowercase.
    toggletitlefalse = models.CharField(db_column='ToggleTitleFalse', max_length=50, blank=True, null=True)  # Field name made lowercase.
    defaultvalue = models.CharField(db_column='DefaultValue', max_length=150, blank=True, null=True)  # Field name made lowercase.
    datetype = models.IntegerField(db_column='DateType', blank=True, null=True)  # Field name made lowercase.
    datealarm = models.BooleanField(db_column='DateAlarm', blank=True, null=True)  # Field name made lowercase.
    comment = models.CharField(db_column='Comment', max_length=250, blank=True, null=True)  # Field name made lowercase.
    createdtime = models.CharField(db_column='CreatedTime', max_length=5, blank=True, null=True)  # Field name made lowercase.
    createddate = models.CharField(db_column='CreatedDate', max_length=10, blank=True, null=True)  # Field name made lowercase.
    modifiedtime = models.CharField(db_column='ModifiedTime', max_length=5, blank=True, null=True)  # Field name made lowercase.
    modifieddate = models.CharField(db_column='ModifiedDate', max_length=10, blank=True, null=True)  # Field name made lowercase.
    usercreated = models.CharField(db_column='UserCreated', max_length=50, blank=True, null=True)  # Field name made lowercase.
    usermodified = models.CharField(db_column='UserModified', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DetailTypes'


class Detailtypesitems(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    detailid = models.ForeignKey(Detailtypes, on_delete=models.DO_NOTHING, db_column='DetailID')  # Field name made lowercase.
    row = models.IntegerField(db_column='Row')  # Field name made lowercase.
    value = models.CharField(db_column='Value', max_length=150)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DetailTypesItems'


class DetailtypesSelectedlistDetail(models.Model):
    sl_code = models.ForeignKey('DetailtypesSelectedlists', on_delete=models.DO_NOTHING, db_column='SL_Code')  # Field name made lowercase.
    code = models.ForeignKey(Detailtypes, on_delete=models.DO_NOTHING, db_column='Code')  # Field name made lowercase.
    radif = models.SmallIntegerField(db_column='Radif', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DetailTypes_SelectedList_Detail'


class DetailtypesSelectedlists(models.Model):
    id = id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    code = models.IntegerField(db_column='Code')  # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=100)  # Field name made lowercase.
    comment = models.CharField(db_column='Comment', max_length=500, blank=True, null=True)  # Field name made lowercase.
    defaultselectedlist = models.BooleanField(db_column='DefaultSelectedList', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DetailTypes_SelectedLists'


class Device(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    devicename = models.CharField(db_column='DeviceName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    deviceid = models.IntegerField(db_column='DeviceID', blank=True, null=True)  # Field name made lowercase.
    devicestate = models.IntegerField(db_column='DeviceState', blank=True, null=True)  # Field name made lowercase.
    deviceport = models.SmallIntegerField(db_column='DevicePort', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Device'


class Devideddetails(models.Model):
    code = models.IntegerField(db_column='Code', primary_key=True)  # Field name made lowercase.
    goodcode = models.IntegerField(db_column='GoodCode')  # Field name made lowercase.
    createddate = models.CharField(db_column='CreatedDate', max_length=10, blank=True, null=True)  # Field name made lowercase.
    usercreated = models.IntegerField(db_column='UserCreated')  # Field name made lowercase.
    global_field = models.ForeignKey('GlobalIds', on_delete=models.DO_NOTHING, db_column='Global_ID', blank=True, null=True)  # Field name made lowercase. Field renamed because it was a Python reserved word.
    operationdate = models.CharField(db_column='OperationDate', max_length=10, blank=True, null=True)  # Field name made lowercase.
    tmp = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'DevidedDetails'


class Diagnosticsystem(models.Model):
    diagid = models.IntegerField(db_column='DiagID', primary_key=True)  # Field name made lowercase.
    type = models.SmallIntegerField(db_column='Type', blank=True, null=True)  # Field name made lowercase.
    diagtype = models.CharField(db_column='DiagType', max_length=20, blank=True, null=True)  # Field name made lowercase.
    comment = models.CharField(db_column='Comment', max_length=150, blank=True, null=True)  # Field name made lowercase.
    subject = models.CharField(db_column='Subject', max_length=150, blank=True, null=True)  # Field name made lowercase.
    diagstate = models.SmallIntegerField(db_column='DiagState', blank=True, null=True)  # Field name made lowercase.
    script = models.TextField(db_column='Script', blank=True, null=True)  # Field name made lowercase.
    visible = models.BooleanField(db_column='Visible')  # Field name made lowercase.
    reccountvisible = models.BooleanField(db_column='RecCountVisible', blank=True, null=True)  # Field name made lowercase.
    resultscript = models.TextField(db_column='ResultScript', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DiagnosticSystem'


class DiagnosticsystemFix(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    diagid = models.IntegerField(db_column='DiagID')  # Field name made lowercase.
    runorder = models.SmallIntegerField(db_column='RunOrder', blank=True, null=True)  # Field name made lowercase.
    diagtype = models.SmallIntegerField(db_column='DiagType', blank=True, null=True, db_comment='1=Run SQL Script | 2=File Down')  # Field name made lowercase.
    solution = models.TextField(db_column='Solution', blank=True, null=True, db_comment='Run SQL Script | File Download')  # Field name made lowercase.
    runas = models.BooleanField(db_column='RunAs', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DiagnosticSystem_Fix'


class DisketBank(models.Model):
    code = models.AutoField(db_column='Code', primary_key=True)  # Field name made lowercase.
    headerformul = models.CharField(db_column='HeaderFormul', max_length=300, blank=True, null=True)  # Field name made lowercase.
    mainformul = models.CharField(db_column='MainFormul', max_length=300, blank=True, null=True)  # Field name made lowercase.
    footerformul = models.CharField(db_column='FooterFormul', max_length=300, blank=True, null=True)  # Field name made lowercase.
    comment = models.CharField(db_column='Comment', max_length=250, blank=True, null=True)  # Field name made lowercase.
    acconuntno = models.CharField(db_column='AcconuntNo', max_length=50, blank=True, null=True)  # Field name made lowercase.
    branchno = models.CharField(db_column='BranchNo', max_length=50, blank=True, null=True)  # Field name made lowercase.
    filename = models.CharField(db_column='FileName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    stagecode = models.IntegerField(db_column='StageCode', blank=True, null=True)  # Field name made lowercase.
    bank_name = models.CharField(max_length=50, blank=True, null=True)
    banktypecode = models.IntegerField(db_column='BankTypecode', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Disket_Bank'


class Electroniccoupongoods(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True, db_comment='کليد جدول')  # Field name made lowercase.
    couponidentity = models.CharField(db_column='CouponIdentity', unique=True, max_length=128, db_comment='کد کالابرگ')  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=128, db_comment='نام کالابرگ')  # Field name made lowercase.
    quantity = models.DecimalField(db_column='Quantity', max_digits=23, decimal_places=8, db_comment='سرانه هر نفر')  # Field name made lowercase.
    unitscode = models.ForeignKey('Units', on_delete=models.DO_NOTHING, db_column='UnitsCode', db_comment='واحد کالابرگ')  # Field name made lowercase.
    creditcost = models.DecimalField(db_column='CreditCost', max_digits=23, decimal_places=8, db_comment='ميزان اعتبار تخصيصي')  # Field name made lowercase.
    comment = models.CharField(db_column='Comment', max_length=512, blank=True, null=True, db_comment='توضيحات کالابرگ')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ElectronicCouponGoods'


class Endorsementcheck(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    banktitle = models.CharField(db_column='BankTitle', max_length=50, blank=True, null=True)  # Field name made lowercase.
    accountnumber = models.CharField(db_column='AccountNumber', max_length=50)  # Field name made lowercase.
    owner = models.CharField(db_column='Owner', max_length=50, blank=True, null=True)  # Field name made lowercase.
    fathername = models.CharField(db_column='FatherName', max_length=30, blank=True, null=True)  # Field name made lowercase.
    idnumber = models.CharField(db_column='IdNumber', max_length=20, blank=True, null=True)  # Field name made lowercase.
    birthdate = models.CharField(db_column='BirthDate', max_length=10, blank=True, null=True)  # Field name made lowercase.
    tel = models.CharField(db_column='Tel', max_length=50, blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'EndorsementCheck'


class Excelmapping(models.Model):
    softwarepart = models.IntegerField(db_column='SoftWarePart')  # Field name made lowercase.
    id =  models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=200, blank=True, null=True)  # Field name made lowercase.
    isdefault = models.SmallIntegerField(blank=True, null=True)
    status = models.SmallIntegerField(db_column='Status', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ExcelMapping'


class Excelmappingdetail(models.Model):
    id = models.IntegerField(db_column='ID',primary_key=True)  # Field name made lowercase.
    propertytitle = models.CharField(db_column='PropertyTitle', max_length=200, blank=True, null=True)  # Field name made lowercase.
    xlcolheader = models.CharField(db_column='XlColHeader', max_length=200, blank=True, null=True)  # Field name made lowercase.
    propertytype = models.CharField(db_column='PropertyType', max_length=50, blank=True, null=True)  # Field name made lowercase.
    type = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ExcelMappingDetail'


class ExceptionLogs(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    errormessage = models.CharField(db_column='ErrorMessage', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    errorclass = models.CharField(db_column='ErrorClass', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    dllstatus = models.CharField(db_column='DLLStatus', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    activeform = models.CharField(db_column='ActiveForm', max_length=100, blank=True, null=True)  # Field name made lowercase.
    regdate = models.CharField(db_column='RegDate', max_length=20, blank=True, null=True)  # Field name made lowercase.
    errorimage = models.BinaryField(db_column='ErrorImage', blank=True, null=True)  # Field name made lowercase.
    appversion = models.DecimalField(db_column='AppVersion', max_digits=23, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    trackingcode = models.BigIntegerField(db_column='TrackingCode', blank=True, null=True)  # Field name made lowercase.
    userid = models.IntegerField(db_column='UserId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Exception_Logs'


class Exit(models.Model):
    code = models.IntegerField(db_column='Code', primary_key=True)  # Field name made lowercase.
    obtaincode = models.ForeignKey('Obtain', on_delete=models.DO_NOTHING, db_column='ObtainCode')  # Field name made lowercase.
    date = models.CharField(db_column='Date', max_length=10)  # Field name made lowercase.
    exittype = models.SmallIntegerField(db_column='ExitType')  # Field name made lowercase.
    reciever = models.IntegerField(db_column='Reciever')  # Field name made lowercase.
    amount = models.DecimalField(db_column='Amount', max_digits=23, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    cost = models.DecimalField(db_column='Cost', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    value = models.DecimalField(db_column='Value', max_digits=23, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    comment = models.CharField(db_column='Comment', max_length=500, blank=True, null=True)  # Field name made lowercase.
    benefitcode = models.IntegerField(db_column='BenefitCode', blank=True, null=True)  # Field name made lowercase.
    vouchercode = models.IntegerField(db_column='VoucherCode', blank=True, null=True)  # Field name made lowercase.
    expcentercode = models.IntegerField(db_column='ExpCenterCode', blank=True, null=True)  # Field name made lowercase.
    usercreated = models.IntegerField(db_column='UserCreated')  # Field name made lowercase.
    createddate = models.CharField(db_column='CreatedDate', max_length=10)  # Field name made lowercase.
    createdtime = models.CharField(db_column='CreatedTime', max_length=5)  # Field name made lowercase.
    modifiedtime = models.CharField(db_column='ModifiedTime', max_length=5, blank=True, null=True)  # Field name made lowercase.
    modifieddate = models.CharField(db_column='ModifiedDate', max_length=10, blank=True, null=True)  # Field name made lowercase.
    usermodified = models.IntegerField(db_column='UserModified', blank=True, null=True)  # Field name made lowercase.
    owner = models.IntegerField(db_column='Owner')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Exit'


class Faq(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    keyworld = models.CharField(db_column='KeyWorld', max_length=100)  # Field name made lowercase.
    question = models.CharField(db_column='Question', max_length=200)  # Field name made lowercase.
    answer = models.CharField(db_column='Answer', max_length=500)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FAQ'


class FactprintDetail(models.Model):
    sharh = models.CharField(db_column='Sharh', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    meghdar2 = models.DecimalField(db_column='Meghdar2', max_digits=23, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    meghdar = models.DecimalField(db_column='Meghdar', max_digits=23, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    naghdi = models.DecimalField(db_column='Naghdi', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    mabkol = models.DecimalField(db_column='MabKol', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    code = models.IntegerField(db_column='Code', blank=True, null=True)  # Field name made lowercase.
    type = models.SmallIntegerField(db_column='Type', blank=True, null=True)  # Field name made lowercase.
    kalaname = models.CharField(db_column='KalaName', max_length=200, blank=True, null=True)  # Field name made lowercase.
    unit = models.CharField(db_column='Unit', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FactPrint_Detail'


class FactFo(models.Model):
    code = models.IntegerField(db_column='Code', primary_key=True)  # Field name made lowercase.
    shakhs_code = models.ForeignKey('Perinf', on_delete=models.DO_NOTHING, db_column='Shakhs_Code')  # Field name made lowercase.
    visitor_code = models.ForeignKey('Perinf', on_delete=models.DO_NOTHING, db_column='visitor_code', related_name='factfo_visitor_code_set', blank=True, null=True)
    tavasot = models.CharField(max_length=50, blank=True, null=True)
    tarikh = models.CharField(max_length=10)
    mablagh_factor = models.DecimalField(max_digits=23, decimal_places=9, blank=True, null=True)
    takhfif = models.DecimalField(max_digits=23, decimal_places=9, blank=True, null=True)
    ranandeh_code = models.IntegerField(blank=True, null=True)
    mablagh_haml = models.DecimalField(max_digits=23, decimal_places=9, blank=True, null=True)
    sanad_code = models.IntegerField(blank=True, null=True)
    sharh = models.CharField(max_length=500, blank=True, null=True)
    sabt_hazineh = models.SmallIntegerField(db_column='Sabt_Hazineh', blank=True, null=True)  # Field name made lowercase.
    mablagh_visit = models.DecimalField(db_column='Mablagh_visit', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    status = models.SmallIntegerField(blank=True, null=True)
    sanad = models.IntegerField(blank=True, null=True)
    tarikhvosoul = models.CharField(max_length=10, blank=True, null=True)
    tasviye = models.SmallIntegerField(blank=True, null=True)
    naghdi = models.SmallIntegerField(blank=True, null=True)
    lockfact = models.SmallIntegerField(db_column='LockFact', blank=True, null=True)  # Field name made lowercase.
    com_index = models.IntegerField(db_column='Com_Index')  # Field name made lowercase.
    extname = models.CharField(db_column='extName', max_length=150, blank=True, null=True)  # Field name made lowercase.
    charge = models.DecimalField(db_column='Charge', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    tax = models.DecimalField(db_column='Tax', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    fishnum = models.IntegerField(db_column='FishNum', blank=True, null=True)  # Field name made lowercase.
    rst_comment = models.CharField(db_column='Rst_Comment', max_length=500, blank=True, null=True)  # Field name made lowercase.
    rst_indoor = models.BooleanField(db_column='Rst_Indoor', blank=True, null=True)  # Field name made lowercase.
    last_print_date = models.CharField(db_column='Last_Print_Date', max_length=10, blank=True, null=True)  # Field name made lowercase.
    expcentercode = models.IntegerField(db_column='ExpCenterCode', blank=True, null=True)  # Field name made lowercase.
    facttakhfif_vis = models.DecimalField(db_column='FactTakhfif_Vis', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    refrenceid = models.CharField(db_column='RefrenceID', max_length=8000, blank=True, null=True)  # Field name made lowercase.
    currcode = models.IntegerField(db_column='CurrCode', blank=True, null=True)  # Field name made lowercase.
    currrate = models.DecimalField(db_column='CurrRate', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    global_field = models.ForeignKey('GlobalIds', on_delete=models.DO_NOTHING, db_column='Global_ID', blank=True, null=True)  # Field name made lowercase. Field renamed because it was a Python reserved word.
    tarikhtahvil = models.CharField(db_column='TarikhTahvil', max_length=10, blank=True, null=True)  # Field name made lowercase.
    tahvil = models.BooleanField(db_column='Tahvil', blank=True, null=True)  # Field name made lowercase.
    noetasviye = models.SmallIntegerField(db_column='NoeTasviye', blank=True, null=True)  # Field name made lowercase.
    createdtime = models.CharField(db_column='CreatedTime', max_length=5, blank=True, null=True)  # Field name made lowercase.
    createddate = models.CharField(db_column='CreatedDate', max_length=10, blank=True, null=True)  # Field name made lowercase.
    modifiedtime = models.CharField(db_column='ModifiedTime', max_length=5, blank=True, null=True)  # Field name made lowercase.
    modifieddate = models.CharField(db_column='ModifiedDate', max_length=10, blank=True, null=True)  # Field name made lowercase.
    usercreated = models.IntegerField(db_column='UserCreated')  # Field name made lowercase.
    usermodified = models.IntegerField(db_column='UserModified', blank=True, null=True)  # Field name made lowercase.
    ranandeh_isperson = models.BooleanField(db_column='Ranandeh_IsPerson', blank=True, null=True)  # Field name made lowercase.
    takhfif_type = models.BooleanField(db_column='Takhfif_Type', blank=True, null=True)  # Field name made lowercase.
    takhfif_percent = models.DecimalField(db_column='Takhfif_Percent', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    salereasonid = models.IntegerField(db_column='SaleReasonID', blank=True, null=True)  # Field name made lowercase.
    roundfactprice_use = models.BooleanField(db_column='RoundFactPrice_Use')  # Field name made lowercase.
    roundfactprice = models.DecimalField(db_column='RoundFactPrice', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    visitorcurrtype = models.BooleanField(db_column='VisitorCurrType', blank=True, null=True)  # Field name made lowercase.
    ranandehcurrtype = models.BooleanField(db_column='RanandehCurrType', blank=True, null=True)  # Field name made lowercase.
    addrtitle = models.CharField(db_column='AddrTitle', max_length=100, blank=True, null=True)  # Field name made lowercase.
    addrdescription = models.CharField(db_column='AddrDescription', max_length=500, blank=True, null=True)  # Field name made lowercase.
    addrcitycode = models.IntegerField(db_column='AddrCityCode', blank=True, null=True)  # Field name made lowercase.
    addraddress = models.CharField(db_column='AddrAddress', max_length=500, blank=True, null=True)  # Field name made lowercase.
    addrtel = models.CharField(db_column='AddrTel', max_length=15, blank=True, null=True)  # Field name made lowercase.
    addrmobile = models.CharField(db_column='AddrMobile', max_length=15, blank=True, null=True)  # Field name made lowercase.
    addrpostalcode = models.CharField(db_column='AddrPostalCode', max_length=10, blank=True, null=True)  # Field name made lowercase.
    addrlatitude = models.DecimalField(db_column='AddrLatitude', max_digits=23, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    addrlongitude = models.DecimalField(db_column='AddrLongitude', max_digits=23, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    owner = models.IntegerField(db_column='Owner')  # Field name made lowercase.
    salespatterntype = models.SmallIntegerField(db_column='SalesPatternType')  # Field name made lowercase.
    cottagenumber = models.CharField(db_column='CottageNumber', max_length=14, blank=True, null=True)  # Field name made lowercase.
    cottagedate = models.CharField(db_column='CottageDate', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Fact_Fo'


# accounting/models.py

# ... (مدل FactFo باید بالاتر از این تعریف شده باشد) ...

class FactFoDetail(models.Model):
    # این فیلد کلید اصلی مجازی ما برای جنگو است
    pk_for_django = models.BigAutoField(primary_key=True)

    # فیلد code باید ForeignKey باشد و primary_key=True نداشته باشد
    code = models.ForeignKey(FactFo, on_delete=models.DO_NOTHING, db_column='code')
    radif = models.SmallIntegerField()
    an_code = models.SmallIntegerField(blank=True, null=True)
    kala_code = models.IntegerField()
    sharh = models.CharField(max_length=500, blank=True, null=True)
    meghdar = models.DecimalField(max_digits=23, decimal_places=8, blank=True, null=True)
    naghdi = models.DecimalField(max_digits=23, decimal_places=9, blank=True, null=True)
    reval = models.IntegerField(blank=True, null=True)
    vaziyat = models.SmallIntegerField()
    status = models.SmallIntegerField(blank=True, null=True)
    type = models.SmallIntegerField(db_column='Type', blank=True, null=True)
    darsad_vis = models.DecimalField(max_digits=23, decimal_places=8, blank=True, null=True)
    tool = models.DecimalField(max_digits=23, decimal_places=8, blank=True, null=True)
    arz = models.DecimalField(max_digits=23, decimal_places=8, blank=True, null=True)
    tedad = models.IntegerField(blank=True, null=True)
    meghdar2 = models.DecimalField(max_digits=23, decimal_places=8, blank=True, null=True)
    ghotr = models.DecimalField(max_digits=23, decimal_places=8, blank=True, null=True)
    com_index = models.IntegerField()
    toolidcode = models.IntegerField(db_column='ToolidCode', blank=True, null=True)
    userprice = models.DecimalField(db_column='UserPrice', max_digits=23, decimal_places=9, blank=True, null=True)
    chargepercent = models.DecimalField(db_column='ChargePercent', max_digits=23, decimal_places=8, blank=True, null=True)
    taxpercent = models.DecimalField(db_column='TaxPercent', max_digits=23, decimal_places=8, blank=True, null=True)
    takhfif = models.DecimalField(max_digits=23, decimal_places=9, blank=True, null=True)
    ordercode = models.ForeignKey('Order', on_delete=models.DO_NOTHING, db_column='OrderCode', blank=True, null=True)
    takhfiftype = models.BooleanField(db_column='TakhfifType')
    takhfifasexpense = models.BooleanField(db_column='TakhfifAsExpense', blank=True, null=True)
    off_user = models.DecimalField(db_column='Off_User', max_digits=23, decimal_places=9, blank=True, null=True)
    off_sys = models.DecimalField(db_column='Off_Sys', max_digits=23, decimal_places=9, blank=True, null=True)
    cost_entery_type = models.BooleanField(db_column='Cost_Entery_Type', blank=True, null=True)
    totalcost = models.DecimalField(db_column='TotalCost', max_digits=23, decimal_places=9, blank=True, null=True)
    currcode = models.IntegerField(db_column='CurrCode', blank=True, null=True)
    currrate = models.DecimalField(db_column='CurrRate', max_digits=23, decimal_places=9, blank=True, null=True)
    barcode = models.CharField(db_column='Barcode', max_length=50, blank=True, null=True)
    gifttype = models.SmallIntegerField(db_column='GiftType', blank=True, null=True)
    promotioncode = models.IntegerField(db_column='PromotionCode', blank=True, null=True)
    offvaluetype = models.SmallIntegerField(db_column='OffValueType', blank=True, null=True)
    goldprice = models.DecimalField(db_column='GoldPrice', max_digits=23, decimal_places=9, blank=True, null=True)
    wages = models.DecimalField(db_column='Wages', max_digits=23, decimal_places=9, blank=True, null=True)
    sellerprofit = models.DecimalField(db_column='SellerProfit', max_digits=23, decimal_places=9, blank=True, null=True)
    rightofaction = models.DecimalField(db_column='RightOfAction', max_digits=23, decimal_places=9, blank=True, null=True)
    goldselltaxpercent = models.DecimalField(db_column='GoldSellTaxPercent', max_digits=23, decimal_places=8, blank=True, null=True)
    currencytype = models.CharField(db_column='CurrencyType', max_length=3, blank=True, null=True)
    exchangeratewithrial = models.DecimalField(db_column='ExchangeRateWithRial', max_digits=23, decimal_places=9, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Fact_Fo_Detail'
        unique_together = (('code', 'radif'),)

class FactVisitor(models.Model):
    id = id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    fact_code = models.IntegerField(blank=True, null=True)
    per_code = models.IntegerField(db_column='Per_code', blank=True, null=True)  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=50, blank=True, null=True)  # Field name made lowercase.
    percent = models.DecimalField(db_column='Percent', max_digits=23, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    price = models.DecimalField(db_column='Price', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    tmp = models.BooleanField(blank=True, null=True)
    type_pay = models.BooleanField(blank=True, null=True)
    currtype = models.BooleanField(db_column='CurrType', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Fact_Visitor'


class Factsreport(models.Model):
    kala_code = models.IntegerField(db_column='Kala_Code', blank=True, null=True)  # Field name made lowercase.
    tedad1 = models.DecimalField(db_column='Tedad1', max_digits=23, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    tedad2 = models.DecimalField(db_column='Tedad2', max_digits=23, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    factcode = models.IntegerField(db_column='FactCode', blank=True, null=True)  # Field name made lowercase.
    naghdi = models.DecimalField(db_column='Naghdi', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    type = models.SmallIntegerField(db_column='Type', blank=True, null=True)  # Field name made lowercase.
    anbar_code = models.IntegerField(db_column='Anbar_Code', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FactsReport'


class Fieldsvalueslist(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True, db_comment='کليد اصلي')  # Field name made lowercase.
    tablesfieldslistid = models.ForeignKey('Tablesfieldslist', on_delete=models.DO_NOTHING, db_column='TablesFieldsListID', db_comment='کليد فرعي ليست فيلد')  # Field name made lowercase.
    fieldvalue = models.IntegerField(db_column='FieldValue', db_comment='مقدار فيلد')  # Field name made lowercase.
    valuecaption = models.CharField(db_column='ValueCaption', max_length=200, db_comment='کپشن مقدار فيلد')  # Field name made lowercase.
    isdefult = models.BooleanField(db_column='IsDefult', db_comment='پيش فرض است')  # Field name made lowercase.
    isactive = models.BooleanField(db_column='IsActive', db_comment='فعال است')  # Field name made lowercase.
    comment = models.CharField(db_column='Comment', max_length=500, blank=True, null=True, db_comment='توضيحات')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FieldsValuesList'


class Financialreport(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    kol = models.IntegerField(db_column='Kol')  # Field name made lowercase.
    moin = models.IntegerField(db_column='Moin', blank=True, null=True)  # Field name made lowercase.
    tafsili = models.IntegerField(db_column='Tafsili', blank=True, null=True)  # Field name made lowercase.
    rownum = models.SmallIntegerField(db_column='RowNum')  # Field name made lowercase.
    type = models.SmallIntegerField(db_column='Type')  # Field name made lowercase.
    alias = models.CharField(db_column='Alias', max_length=200, blank=True, null=True)  # Field name made lowercase.
    options = models.BooleanField(db_column='Options')  # Field name made lowercase.
    reportcode = models.IntegerField(db_column='ReportCode', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FinancialReport'


class Financialreportdetail(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    fr_id = models.IntegerField(db_column='FR_ID')  # Field name made lowercase.
    kol = models.IntegerField(db_column='Kol')  # Field name made lowercase.
    moin = models.IntegerField(db_column='Moin', blank=True, null=True)  # Field name made lowercase.
    tafsili = models.IntegerField(db_column='Tafsili', blank=True, null=True)  # Field name made lowercase.
    type = models.SmallIntegerField(db_column='Type')  # Field name made lowercase.
    dec = models.BooleanField(db_column='Dec', blank=True, null=True)  # Field name made lowercase.
    tmp = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'FinancialReportDetail'


class Financialreporttitle(models.Model):
    reportid = models.AutoField(db_column='ReportId',primary_key=True)  # Field name made lowercase.
    reporttitle = models.CharField(db_column='ReportTitle', max_length=150)  # Field name made lowercase.
    reporttype = models.SmallIntegerField(db_column='ReportType')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FinancialReportTitle'


class Financialstatements(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    kol = models.IntegerField(db_column='Kol')  # Field name made lowercase.
    moin = models.IntegerField(db_column='Moin', blank=True, null=True)  # Field name made lowercase.
    tafsili = models.IntegerField(db_column='Tafsili', blank=True, null=True)  # Field name made lowercase.
    rownum = models.SmallIntegerField(db_column='RowNum')  # Field name made lowercase.
    type = models.SmallIntegerField(db_column='Type')  # Field name made lowercase.
    alias = models.CharField(db_column='Alias', max_length=200, blank=True, null=True)  # Field name made lowercase.
    options = models.BooleanField(db_column='Options')  # Field name made lowercase.
    reportcode = models.IntegerField(db_column='ReportCode', blank=True, null=True)  # Field name made lowercase.
    rowstyle = models.SmallIntegerField(db_column='RowStyle')  # Field name made lowercase.
    istopline = models.BooleanField(db_column='IsTopLine')  # Field name made lowercase.
    personsacccalctype = models.SmallIntegerField(db_column='PersonsAccCalcType')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FinancialStatements'


class Financialstatementsdetail(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    fr_id = models.IntegerField(db_column='FR_ID')  # Field name made lowercase.
    kol = models.IntegerField(db_column='Kol')  # Field name made lowercase.
    moin = models.IntegerField(db_column='Moin', blank=True, null=True)  # Field name made lowercase.
    tafsili = models.IntegerField(db_column='Tafsili', blank=True, null=True)  # Field name made lowercase.
    type = models.SmallIntegerField(db_column='Type')  # Field name made lowercase.
    dec = models.BooleanField(db_column='Dec', blank=True, null=True)  # Field name made lowercase.
    tmp = models.BooleanField(blank=True, null=True)
    personsacccalctype = models.SmallIntegerField(db_column='PersonsAccCalcType')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FinancialStatementsDetail'


class Financialstatementstitle(models.Model):
    reportid = models.AutoField(db_column='ReportId',primary_key=True)  # Field name made lowercase.
    reporttitle = models.CharField(db_column='ReportTitle', max_length=150)  # Field name made lowercase.
    reporttype = models.SmallIntegerField(db_column='ReportType')  # Field name made lowercase.
    isifrs = models.BooleanField(db_column='IsIFRS')  # Field name made lowercase.
    issystemrecord = models.BooleanField(db_column='IsSystemRecord')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FinancialStatementsTitle'


class Fineandreward(models.Model):
    code = models.IntegerField(db_column='Code', primary_key=True)  # Field name made lowercase.
    salarybillcode = models.IntegerField(db_column='SalaryBillCode')  # Field name made lowercase.
    type = models.IntegerField(db_column='Type')  # Field name made lowercase.
    staffcode = models.ForeignKey('Staff', on_delete=models.DO_NOTHING, db_column='StaffCode')  # Field name made lowercase.
    date = models.CharField(db_column='Date', max_length=10)  # Field name made lowercase.
    cost = models.DecimalField(db_column='Cost', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    comment = models.CharField(db_column='Comment', max_length=500, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FineAndReward'


class Fiscal(models.Model):
    code = models.IntegerField(db_column='Code', primary_key=True)  # Field name made lowercase.
    title = models.CharField(db_column='Title', unique=True, max_length=50)  # Field name made lowercase.
    cost = models.DecimalField(db_column='Cost', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    tax = models.BooleanField(db_column='Tax')  # Field name made lowercase.
    insurance = models.BooleanField(db_column='Insurance')  # Field name made lowercase.
    comment = models.CharField(db_column='Comment', max_length=500, blank=True, null=True)  # Field name made lowercase.
    calctype = models.SmallIntegerField(db_column='CalcType')  # Field name made lowercase.
    grpcode = models.ForeignKey('Fiscalgrp', on_delete=models.DO_NOTHING, db_column='GrpCode')  # Field name made lowercase.
    kol = models.SmallIntegerField(db_column='Kol', blank=True, null=True)  # Field name made lowercase.
    moin = models.SmallIntegerField(db_column='Moin', blank=True, null=True)  # Field name made lowercase.
    tafzili = models.IntegerField(db_column='Tafzili', blank=True, null=True)  # Field name made lowercase.
    createdtime = models.CharField(db_column='CreatedTime', max_length=5)  # Field name made lowercase.
    createddate = models.CharField(db_column='CreatedDate', max_length=10)  # Field name made lowercase.
    usercreated = models.IntegerField(db_column='UserCreated')  # Field name made lowercase.
    modifiedtime = models.CharField(db_column='ModifiedTime', max_length=5, blank=True, null=True)  # Field name made lowercase.
    modifieddate = models.CharField(db_column='ModifiedDate', max_length=10, blank=True, null=True)  # Field name made lowercase.
    usermodified = models.IntegerField(db_column='UserModified', blank=True, null=True)  # Field name made lowercase.
    owner = models.IntegerField(db_column='Owner')  # Field name made lowercase.
    iscontinuous = models.BooleanField(db_column='IsContinuous')  # Field name made lowercase.
    iscash = models.BooleanField(db_column='IsCash')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Fiscal'


class Fiscalgrp(models.Model):
    code = models.IntegerField(db_column='Code', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', unique=True, max_length=50)  # Field name made lowercase.
    comment = models.CharField(db_column='Comment', max_length=500, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FiscalGrp'


class Fiscalyear(models.Model):
    title = models.CharField(db_column='Title', unique=True, max_length=50)  # Field name made lowercase.
    active = models.BooleanField(db_column='Active')  # Field name made lowercase.
    comment = models.CharField(db_column='Comment', max_length=500, blank=True, null=True)  # Field name made lowercase.
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    dbname = models.CharField(db_column='DBName', max_length=150, blank=True, null=True)  # Field name made lowercase.
    datestart = models.CharField(db_column='DateStart', max_length=10, blank=True, null=True)  # Field name made lowercase.
    dateend = models.CharField(db_column='DateEnd', max_length=10, blank=True, null=True)  # Field name made lowercase.
    closetype = models.SmallIntegerField(db_column='CloseType', blank=True, null=True)  # Field name made lowercase.
    chektemplet = models.IntegerField(db_column='ChekTemplet', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FiscalYear'


class Fiscalyearcheck(models.Model):
    id_check = models.CharField(db_column='ID_CHeck', max_length=50, blank=True, null=True)  # Field name made lowercase.
    date2 = models.CharField(db_column='Date2', max_length=10, blank=True, null=True)  # Field name made lowercase.
    status = models.SmallIntegerField(db_column='Status', blank=True, null=True)  # Field name made lowercase.
    perid = models.IntegerField(db_column='PerId', blank=True, null=True)  # Field name made lowercase.
    date1 = models.CharField(db_column='Date1', max_length=10, blank=True, null=True)  # Field name made lowercase.
    amount = models.DecimalField(db_column='Amount', max_digits=23, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    comment = models.CharField(db_column='Comment', max_length=500, blank=True, null=True)  # Field name made lowercase.
    bankcode = models.IntegerField(db_column='BankCode', blank=True, null=True)  # Field name made lowercase.
    pertype = models.SmallIntegerField(db_column='PerType', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FiscalYearCheck'


class FisclyearChecklist(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    sharh = models.CharField(db_column='Sharh', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FisclYear_CheckList'


class Floatingaccounts(models.Model):
    id = id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    floatingaccountsgroupsid = models.ForeignKey('Floatingaccountsgroups', on_delete=models.DO_NOTHING, db_column='FloatingAccountsGroupsID')  # Field name made lowercase.
    code = models.IntegerField(db_column='Code')  # Field name made lowercase.
    searchid = models.IntegerField(db_column='SearchID', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=128)  # Field name made lowercase.
    comment = models.CharField(db_column='Comment', max_length=512, blank=True, null=True)  # Field name made lowercase.
    createdtime = models.CharField(db_column='CreatedTime', max_length=5)  # Field name made lowercase.
    createddate = models.CharField(db_column='CreatedDate', max_length=10)  # Field name made lowercase.
    modifiedtime = models.CharField(db_column='ModifiedTime', max_length=5, blank=True, null=True)  # Field name made lowercase.
    modifieddate = models.CharField(db_column='ModifiedDate', max_length=10, blank=True, null=True)  # Field name made lowercase.
    usercreated = models.IntegerField(db_column='UserCreated')  # Field name made lowercase.
    usermodified = models.IntegerField(db_column='UserModified', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FloatingAccounts'


class Floatingaccountsgroups(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    code = models.IntegerField(db_column='Code', unique=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=128)  # Field name made lowercase.
    comment = models.CharField(db_column='Comment', max_length=512, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FloatingAccountsGroups'


class Gdaramad(models.Model):
    code = models.SmallIntegerField(db_column='Code', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=50, blank=True, null=True)  # Field name made lowercase.
    comment = models.CharField(db_column='Comment', max_length=500, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'GDaramad'


class Grpgallery(models.Model):
    code = models.IntegerField(db_column='Code', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=50, blank=True, null=True)  # Field name made lowercase.
    comment = models.CharField(db_column='Comment', max_length=500, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'GRPGallery'


class GHazine(models.Model):
    code = models.IntegerField(db_column='Code', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=50, blank=True, null=True)  # Field name made lowercase.
    comment = models.CharField(db_column='Comment', max_length=500, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'G_Hazine'


class GardeshAshkhas(models.Model):
    code = models.CharField(db_column='Code', max_length=50)  # Field name made lowercase. The composite primary key (Code, PerCode, Type, Sanad_Code, Type_Gar) found, that is not supported. The first column is selected.
    percode = models.IntegerField(db_column='PerCode')  # Field name made lowercase.
    type = models.SmallIntegerField(db_column='Type')  # Field name made lowercase.
    date = models.CharField(db_column='Date', max_length=10, blank=True, null=True)  # Field name made lowercase.
    sanad_code = models.IntegerField(db_column='Sanad_Code')  # Field name made lowercase.
    type_gar = models.SmallIntegerField(db_column='Type_Gar')  # Field name made lowercase.
    amount = models.DecimalField(db_column='Amount', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    radif = models.BigAutoField(db_column='Radif', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Gardesh_Ashkhas'
        unique_together = (('code', 'percode', 'type', 'sanad_code', 'type_gar'),)


class GetRecieve(models.Model):
    code = models.IntegerField(db_column='Code', primary_key=True)  # Field name made lowercase. The composite primary key (Code, Type) found, that is not supported. The first column is selected.
    percode = models.IntegerField(db_column='PerCode')  # Field name made lowercase.
    amount = models.DecimalField(db_column='Amount', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    comment = models.CharField(db_column='Comment', max_length=500, blank=True, null=True)  # Field name made lowercase.
    date = models.CharField(db_column='Date', max_length=10)  # Field name made lowercase.
    status = models.SmallIntegerField(db_column='Status', blank=True, null=True)  # Field name made lowercase.
    type = models.SmallIntegerField(db_column='Type')  # Field name made lowercase.
    fish = models.CharField(db_column='Fish', max_length=50, blank=True, null=True)  # Field name made lowercase.
    op_type = models.SmallIntegerField(db_column='OP_Type')  # Field name made lowercase.
    lmod = models.DecimalField(db_column='LMod', max_digits=23, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    jam = models.DecimalField(db_column='Jam', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    takhfif = models.DecimalField(db_column='Takhfif', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    lsit = models.SmallIntegerField(blank=True, null=True)
    status_fact = models.IntegerField(db_column='Status_Fact', blank=True, null=True)  # Field name made lowercase.
    sandogh_code = models.ForeignKey('SandoghTbl', on_delete=models.DO_NOTHING, db_column='Sandogh_Code', blank=True, null=True)  # Field name made lowercase.
    tavasot = models.CharField(db_column='Tavasot', max_length=50, blank=True, null=True)  # Field name made lowercase.
    vouchercode = models.IntegerField(db_column='VoucherCode', blank=True, null=True)  # Field name made lowercase.
    owner_type = models.SmallIntegerField(db_column='Owner_Type', blank=True, null=True)  # Field name made lowercase.
    visitor_code = models.IntegerField(db_column='Visitor_Code', blank=True, null=True)  # Field name made lowercase.
    expcentercode = models.IntegerField(db_column='ExpCenterCode', blank=True, null=True)  # Field name made lowercase.
    refrenceid = models.CharField(db_column='RefrenceID', max_length=8000, blank=True, null=True)  # Field name made lowercase.
    flag = models.SmallIntegerField(blank=True, null=True)
    currcode = models.IntegerField(db_column='CurrCode', blank=True, null=True)  # Field name made lowercase.
    currrate = models.DecimalField(db_column='CurrRate', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    createdtime = models.CharField(db_column='CreatedTime', max_length=5, blank=True, null=True)  # Field name made lowercase.
    createddate = models.CharField(db_column='CreatedDate', max_length=10, blank=True, null=True)  # Field name made lowercase.
    modifiedtime = models.CharField(db_column='ModifiedTime', max_length=5, blank=True, null=True)  # Field name made lowercase.
    modifieddate = models.CharField(db_column='ModifiedDate', max_length=10, blank=True, null=True)  # Field name made lowercase.
    usercreated = models.IntegerField(db_column='UserCreated')  # Field name made lowercase.
    usermodified = models.IntegerField(db_column='UserModified', blank=True, null=True)  # Field name made lowercase.
    global_id = models.IntegerField(db_column='Global_ID')  # Field name made lowercase.
    owner = models.IntegerField(db_column='Owner')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Get_Recieve'
        unique_together = (('code', 'type'),)


class GlobalIds(models.Model):
    softwarepart = models.IntegerField(db_column='SoftwarePart')
    code = models.IntegerField(db_column='Code')
    order = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'Global_IDs'


class Goodconsign(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    code = models.IntegerField(db_column='Code')  # Field name made lowercase.
    per_code = models.ForeignKey('Perinf', on_delete=models.DO_NOTHING, db_column='Per_Code')  # Field name made lowercase.
    good_code = models.ForeignKey('Goodinf', on_delete=models.DO_NOTHING, db_column='Good_Code')  # Field name made lowercase.
    store_code = models.ForeignKey('Stores', on_delete=models.DO_NOTHING, db_column='Store_Code')  # Field name made lowercase.
    date = models.CharField(db_column='Date', max_length=10)  # Field name made lowercase.
    return_date = models.CharField(db_column='Return_Date', max_length=10, blank=True, null=True)  # Field name made lowercase.
    amount1 = models.DecimalField(db_column='Amount1', max_digits=23, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    amount2 = models.DecimalField(db_column='Amount2', max_digits=23, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    length = models.DecimalField(db_column='Length', max_digits=23, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    width = models.DecimalField(db_column='Width', max_digits=23, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    count = models.IntegerField(db_column='Count', blank=True, null=True)  # Field name made lowercase.
    consign_type = models.SmallIntegerField(db_column='Consign_Type')  # Field name made lowercase.
    operation_type = models.SmallIntegerField(db_column='Operation_Type')  # Field name made lowercase.
    comment = models.CharField(db_column='Comment', max_length=500, blank=True, null=True)  # Field name made lowercase.
    ownerconsign_code = models.IntegerField(db_column='OwnerConsign_Code', blank=True, null=True)  # Field name made lowercase.
    createdtime = models.CharField(db_column='CreatedTime', max_length=5)  # Field name made lowercase.
    createddate = models.CharField(db_column='CreatedDate', max_length=10)  # Field name made lowercase.
    modifiedtime = models.CharField(db_column='ModifiedTime', max_length=5, blank=True, null=True)  # Field name made lowercase.
    modifieddate = models.CharField(db_column='ModifiedDate', max_length=10, blank=True, null=True)  # Field name made lowercase.
    usercreated = models.IntegerField(db_column='UserCreated')  # Field name made lowercase.
    usermodified = models.IntegerField(db_column='UserModified', blank=True, null=True)  # Field name made lowercase.
    owner = models.IntegerField(db_column='Owner')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'GoodConsign'


class Goodcostdiscount(models.Model):
    goodcode = models.IntegerField(db_column='GoodCode', unique=True)  # Field name made lowercase.
    discount_sell_1 = models.DecimalField(db_column='Discount_Sell_1', max_digits=23, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    discount_sell_2 = models.DecimalField(db_column='Discount_Sell_2', max_digits=23, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    discount_sell_3 = models.DecimalField(db_column='Discount_Sell_3', max_digits=23, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    discount_sell_4 = models.DecimalField(db_column='Discount_Sell_4', max_digits=23, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    discount_buy_1 = models.DecimalField(db_column='Discount_Buy_1', max_digits=23, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    discount_buy_2 = models.DecimalField(db_column='Discount_Buy_2', max_digits=23, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    discount_buy_3 = models.DecimalField(db_column='Discount_Buy_3', max_digits=23, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    discount_buy_4 = models.DecimalField(db_column='Discount_Buy_4', max_digits=23, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    default_discount_sell_number = models.IntegerField(db_column='Default_Discount_Sell_Number')  # Field name made lowercase.
    default_discount_buy_number = models.IntegerField(db_column='Default_Discount_Buy_Number')  # Field name made lowercase.
    costlevel_sell_1 = models.DecimalField(db_column='CostLevel_Sell_1', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    costlevel_sell_2 = models.DecimalField(db_column='CostLevel_Sell_2', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    costlevel_sell_3 = models.DecimalField(db_column='CostLevel_Sell_3', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    costlevel_sell_4 = models.DecimalField(db_column='CostLevel_Sell_4', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    costlevel_sell_5 = models.DecimalField(db_column='CostLevel_Sell_5', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    costlevel_sell_6 = models.DecimalField(db_column='CostLevel_Sell_6', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    costlevel_sell_7 = models.DecimalField(db_column='CostLevel_Sell_7', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    costlevel_sell_8 = models.DecimalField(db_column='CostLevel_Sell_8', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    costlevel_sell_9 = models.DecimalField(db_column='CostLevel_Sell_9', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    costlevel_sell_10 = models.DecimalField(db_column='CostLevel_Sell_10', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    costlevel_buy_1 = models.DecimalField(db_column='CostLevel_Buy_1', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    costlevel_buy_2 = models.DecimalField(db_column='CostLevel_Buy_2', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    costlevel_buy_3 = models.DecimalField(db_column='CostLevel_Buy_3', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    costlevel_buy_4 = models.DecimalField(db_column='CostLevel_Buy_4', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    costlevel_buy_5 = models.DecimalField(db_column='CostLevel_Buy_5', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    costlevel_buy_6 = models.DecimalField(db_column='CostLevel_Buy_6', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    costlevel_buy_7 = models.DecimalField(db_column='CostLevel_Buy_7', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    costlevel_buy_8 = models.DecimalField(db_column='CostLevel_Buy_8', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    costlevel_buy_9 = models.DecimalField(db_column='CostLevel_Buy_9', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    costlevel_buy_10 = models.DecimalField(db_column='CostLevel_Buy_10', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    default_costlevel_sell_number = models.IntegerField(db_column='Default_CostLevel_Sell_Number')  # Field name made lowercase.
    default_costlevel_buy_number = models.IntegerField(db_column='Default_CostLevel_Buy_Number')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'GoodCostDiscount'


class Gooddetaildivision(models.Model):
    id = id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    code = models.IntegerField(db_column='Code')  # Field name made lowercase.
    date = models.CharField(db_column='Date', max_length=10, blank=True, null=True)  # Field name made lowercase.
    comment = models.CharField(db_column='Comment', max_length=200, blank=True, null=True)  # Field name made lowercase.
    global_field = models.ForeignKey(GlobalIds, on_delete=models.DO_NOTHING, db_column='Global_ID', blank=True, null=True)  # Field name made lowercase. Field renamed because it was a Python reserved word.

    class Meta:
        managed = False
        db_table = 'GoodDetailDivision'


class Gooddetaildivisiondetail(models.Model):
    divisioncode = models.OneToOneField(Gooddetaildivision, on_delete=models.DO_NOTHING, db_column='DivisionCode')
    storecode = models.ForeignKey('Stores', on_delete=models.DO_NOTHING, db_column='StoreCode')  # Field name made lowercase.
    detailvalueid = models.ForeignKey('Gooddetailvalues', on_delete=models.DO_NOTHING, db_column='DetailValueID')  # Field name made lowercase.
    amount1 = models.DecimalField(db_column='Amount1', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    amount2 = models.DecimalField(db_column='Amount2', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    length = models.DecimalField(db_column='Length', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    width = models.DecimalField(db_column='Width', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    amount3 = models.DecimalField(db_column='Amount3', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    operationrow = models.IntegerField(db_column='OperationRow', unique=True)
    comment = models.CharField(db_column='Comment', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'GoodDetailDivisionDetail'
        # این خط تضمین می‌کند که ترکیب این دو فیلد در دیتابیس شما منحصر به فرد است
        unique_together = (('divisioncode', 'operationrow'),)

class Gooddetaildivisiondetailitems(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)
    divisioncode = models.ForeignKey(Gooddetaildivisiondetail, on_delete=models.DO_NOTHING, db_column='DivisionCode', to_field='operationrow', blank=True, null=True)
    divisionrow = models.ForeignKey(Gooddetaildivisiondetail, on_delete=models.DO_NOTHING, db_column='DivisionRow', to_field='operationrow', related_name='gooddetaildivisiondetailitems_divisionrow_set', blank=True, null=True)
    operationrow = models.IntegerField(db_column='OperationRow', blank=True, null=True)  # Field name made lowercase.
    amount1 = models.DecimalField(db_column='Amount1', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    amount2 = models.DecimalField(db_column='Amount2', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    length = models.DecimalField(db_column='Length', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    width = models.DecimalField(db_column='Width', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    amount3 = models.DecimalField(db_column='Amount3', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'GoodDetailDivisionDetailItems'


class Gooddetailformulatolid(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    detailvalueid = models.IntegerField(db_column='DetailValueID')  # Field name made lowercase.
    amount1 = models.DecimalField(db_column='Amount1', max_digits=23, decimal_places=9)  # Field name made lowercase.
    amount2 = models.DecimalField(db_column='Amount2', max_digits=23, decimal_places=9)  # Field name made lowercase.
    length = models.DecimalField(db_column='Length', max_digits=23, decimal_places=9)  # Field name made lowercase.
    width = models.DecimalField(db_column='Width', max_digits=23, decimal_places=9)  # Field name made lowercase.
    amount3 = models.DecimalField(db_column='Amount3', max_digits=23, decimal_places=9)  # Field name made lowercase.
    operationtype = models.SmallIntegerField(db_column='OperationType')  # Field name made lowercase.
    operationcode = models.IntegerField(db_column='OperationCode')  # Field name made lowercase.
    operationrow = models.IntegerField(db_column='OperationRow')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'GoodDetailFormulaTolid'


class Gooddetailkardex(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    detailvalueid = models.ForeignKey('Gooddetailvalues', on_delete=models.DO_NOTHING, db_column='DetailValueID')  # Field name made lowercase.
    storecode = models.IntegerField(db_column='StoreCode')  # Field name made lowercase.
    amount1 = models.DecimalField(db_column='Amount1', max_digits=23, decimal_places=9)  # Field name made lowercase.
    amount2 = models.DecimalField(db_column='Amount2', max_digits=23, decimal_places=9)  # Field name made lowercase.
    length = models.DecimalField(db_column='Length', max_digits=23, decimal_places=9)  # Field name made lowercase.
    width = models.DecimalField(db_column='Width', max_digits=23, decimal_places=9)  # Field name made lowercase.
    amount3 = models.DecimalField(db_column='Amount3', max_digits=23, decimal_places=9)  # Field name made lowercase.
    operationtype = models.SmallIntegerField(db_column='OperationType')  # Field name made lowercase.
    operationcode = models.IntegerField(db_column='OperationCode')  # Field name made lowercase.
    operationrow = models.IntegerField(db_column='OperationRow')  # Field name made lowercase.
    foreignoperationcode = models.IntegerField(db_column='ForeignOperationCode')  # Field name made lowercase.
    foreignoperationrow = models.IntegerField(db_column='ForeignOperationRow', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'GoodDetailKardex'


class GooddetailkardexenterTemp(models.Model):
    id = id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    detailvalueid = models.IntegerField(db_column='DetailValueID', blank=True, null=True)  # Field name made lowercase.
    storecode = models.IntegerField(db_column='StoreCode', blank=True, null=True)  # Field name made lowercase.
    goodcode = models.IntegerField(db_column='GoodCode', blank=True, null=True)  # Field name made lowercase.
    detailtitle1 = models.CharField(db_column='DetailTitle1', max_length=100, blank=True, null=True)  # Field name made lowercase.
    detailtitle2 = models.CharField(db_column='DetailTitle2', max_length=100, blank=True, null=True)  # Field name made lowercase.
    detailtitle3 = models.CharField(db_column='DetailTitle3', max_length=100, blank=True, null=True)  # Field name made lowercase.
    detailtitle4 = models.CharField(db_column='DetailTitle4', max_length=100, blank=True, null=True)  # Field name made lowercase.
    detailtitle5 = models.CharField(db_column='DetailTitle5', max_length=100, blank=True, null=True)  # Field name made lowercase.
    amount1 = models.DecimalField(db_column='Amount1', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    amount2 = models.DecimalField(db_column='Amount2', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    totalamount = models.DecimalField(db_column='TotalAmount', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    length = models.DecimalField(db_column='Length', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    width = models.DecimalField(db_column='Width', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    amount3 = models.DecimalField(db_column='Amount3', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    operationtype = models.SmallIntegerField(db_column='OperationType', blank=True, null=True)  # Field name made lowercase.
    operationcode = models.IntegerField(db_column='OperationCode', blank=True, null=True)  # Field name made lowercase.
    operationrow = models.IntegerField(db_column='OperationRow', blank=True, null=True)  # Field name made lowercase.
    foreignoperationcode = models.IntegerField(db_column='ForeignOperationCode', blank=True, null=True)  # Field name made lowercase.
    tmp = models.SmallIntegerField(db_column='Tmp', blank=True, null=True)  # Field name made lowercase.
    amount1_ret = models.DecimalField(db_column='Amount1_Ret', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    amount2_ret = models.DecimalField(db_column='Amount2_Ret', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    length_ret = models.DecimalField(db_column='Length_Ret', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    width_ret = models.DecimalField(db_column='Width_Ret', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    amount3_ret = models.DecimalField(db_column='Amount3_Ret', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    foreignoperationrow = models.IntegerField(db_column='ForeignOperationRow', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'GoodDetailKardexEnter_Temp'


class GooddetailkardexexitTemp(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    detailvalueid = models.IntegerField(db_column='DetailValueID', blank=True, null=True)  # Field name made lowercase.
    storecode = models.IntegerField(db_column='StoreCode', blank=True, null=True)  # Field name made lowercase.
    goodcode = models.IntegerField(db_column='GoodCode', blank=True, null=True)  # Field name made lowercase.
    anbarcode = models.IntegerField(db_column='AnbarCode', blank=True, null=True)  # Field name made lowercase.
    detailtitle1 = models.CharField(db_column='DetailTitle1', max_length=100, blank=True, null=True)  # Field name made lowercase.
    detailtitle2 = models.CharField(db_column='DetailTitle2', max_length=100, blank=True, null=True)  # Field name made lowercase.
    detailtitle3 = models.CharField(db_column='DetailTitle3', max_length=100, blank=True, null=True)  # Field name made lowercase.
    detailtitle4 = models.CharField(db_column='DetailTitle4', max_length=100, blank=True, null=True)  # Field name made lowercase.
    detailtitle5 = models.CharField(db_column='DetailTitle5', max_length=100, blank=True, null=True)  # Field name made lowercase.
    amount1 = models.DecimalField(db_column='Amount1', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    amount2 = models.DecimalField(db_column='Amount2', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    totalamount = models.DecimalField(db_column='TotalAmount', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    length = models.DecimalField(db_column='Length', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    width = models.DecimalField(db_column='Width', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    amount3 = models.DecimalField(db_column='Amount3', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    amount1_exit = models.DecimalField(db_column='Amount1_Exit', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    amount2_exit = models.DecimalField(db_column='Amount2_Exit', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    totalamount_exit = models.DecimalField(db_column='TotalAmount_Exit', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    length_exit = models.DecimalField(db_column='Length_Exit', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    width_exit = models.DecimalField(db_column='Width_Exit', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    amount3_exit = models.DecimalField(db_column='Amount3_Exit', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    operationtype = models.SmallIntegerField(db_column='OperationType', blank=True, null=True)  # Field name made lowercase.
    operationcode = models.IntegerField(db_column='OperationCode', blank=True, null=True)  # Field name made lowercase.
    operationrow = models.IntegerField(db_column='OperationRow', blank=True, null=True)  # Field name made lowercase.
    foreignoperationcode = models.IntegerField(db_column='ForeignOperationCode', blank=True, null=True)  # Field name made lowercase.
    comindex = models.IntegerField(db_column='ComIndex', blank=True, null=True)  # Field name made lowercase.
    selected = models.BooleanField(db_column='Selected', blank=True, null=True)  # Field name made lowercase.
    tmp = models.SmallIntegerField(db_column='Tmp', blank=True, null=True)  # Field name made lowercase.
    foreignoperationrow = models.IntegerField(db_column='ForeignOperationRow', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'GoodDetailKardexExit_Temp'


class GooddetailkardexprintTemp(models.Model):
    id = id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    detailvalueid = models.IntegerField(db_column='DetailValueID', blank=True, null=True)  # Field name made lowercase.
    storecode = models.IntegerField(db_column='StoreCode', blank=True, null=True)  # Field name made lowercase.
    goodcode = models.IntegerField(db_column='GoodCode', blank=True, null=True)  # Field name made lowercase.
    detailid1 = models.IntegerField(db_column='DetailID1', blank=True, null=True)  # Field name made lowercase.
    detailtitle1 = models.CharField(db_column='DetailTitle1', max_length=100, blank=True, null=True)  # Field name made lowercase.
    detailvalue1 = models.CharField(db_column='DetailValue1', max_length=100, blank=True, null=True)  # Field name made lowercase.
    detailid2 = models.IntegerField(db_column='DetailID2', blank=True, null=True)  # Field name made lowercase.
    detailtitle2 = models.CharField(db_column='DetailTitle2', max_length=100, blank=True, null=True)  # Field name made lowercase.
    detailvalue2 = models.CharField(db_column='DetailValue2', max_length=100, blank=True, null=True)  # Field name made lowercase.
    detailid3 = models.IntegerField(db_column='DetailID3', blank=True, null=True)  # Field name made lowercase.
    detailtitle3 = models.CharField(db_column='DetailTitle3', max_length=100, blank=True, null=True)  # Field name made lowercase.
    detailvalue3 = models.CharField(db_column='DetailValue3', max_length=100, blank=True, null=True)  # Field name made lowercase.
    detailid4 = models.IntegerField(db_column='DetailID4', blank=True, null=True)  # Field name made lowercase.
    detailtitle4 = models.CharField(db_column='DetailTitle4', max_length=100, blank=True, null=True)  # Field name made lowercase.
    detailvalue4 = models.CharField(db_column='DetailValue4', max_length=100, blank=True, null=True)  # Field name made lowercase.
    detailid5 = models.IntegerField(db_column='DetailID5', blank=True, null=True)  # Field name made lowercase.
    detailtitle5 = models.CharField(db_column='DetailTitle5', max_length=100, blank=True, null=True)  # Field name made lowercase.
    detailvalue5 = models.CharField(db_column='DetailValue5', max_length=100, blank=True, null=True)  # Field name made lowercase.
    detailvalues = models.CharField(db_column='DetailValues', max_length=500, blank=True, null=True)  # Field name made lowercase.
    amount1 = models.DecimalField(db_column='Amount1', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    amount2 = models.DecimalField(db_column='Amount2', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    length = models.DecimalField(db_column='Length', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    width = models.DecimalField(db_column='Width', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    amount3 = models.DecimalField(db_column='Amount3', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    operationtype = models.SmallIntegerField(db_column='OperationType', blank=True, null=True)  # Field name made lowercase.
    operationcode = models.IntegerField(db_column='OperationCode', blank=True, null=True)  # Field name made lowercase.
    operationrow = models.IntegerField(db_column='OperationRow', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'GoodDetailKardexPrint_Temp'


class Gooddetailrelation(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    goodcode = models.ForeignKey('Goodinf', on_delete=models.DO_NOTHING, db_column='GoodCode')  # Field name made lowercase.
    detailid = models.IntegerField(db_column='DetailID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'GoodDetailRelation'


class Gooddetailvaluedetails(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    detailvalueid = models.ForeignKey('Gooddetailvalues', on_delete=models.DO_NOTHING, db_column='DetailValueID')  # Field name made lowercase.
    detailid = models.ForeignKey(Detailtypes, on_delete=models.DO_NOTHING, db_column='DetailID')  # Field name made lowercase.
    value = models.CharField(db_column='Value', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'GoodDetailValueDetails'


class Gooddetailvalues(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    goodcode = models.ForeignKey('Goodinf', on_delete=models.DO_NOTHING, db_column='GoodCode')  # Field name made lowercase.
    costlevel1 = models.DecimalField(db_column='CostLevel1', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    costlevel2 = models.DecimalField(db_column='CostLevel2', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    costlevel3 = models.DecimalField(db_column='CostLevel3', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    costlevel4 = models.DecimalField(db_column='CostLevel4', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    costlevel5 = models.DecimalField(db_column='CostLevel5', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    costlevel6 = models.DecimalField(db_column='CostLevel6', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    costlevel7 = models.DecimalField(db_column='CostLevel7', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    costlevel8 = models.DecimalField(db_column='CostLevel8', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    costlevel9 = models.DecimalField(db_column='CostLevel9', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    costlevel10 = models.DecimalField(db_column='CostLevel10', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    tmp = models.BooleanField(db_column='Tmp', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'GoodDetailValues'


class Goodfirstasset(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    goodcode = models.IntegerField(db_column='GoodCode')  # Field name made lowercase.
    storecode = models.ForeignKey('Stores', on_delete=models.DO_NOTHING, db_column='StoreCode')  # Field name made lowercase.
    tmp = models.SmallIntegerField()
    amount1 = models.DecimalField(db_column='Amount1', max_digits=23, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    amount2 = models.DecimalField(db_column='Amount2', max_digits=23, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    comment = models.CharField(db_column='Comment', max_length=500, blank=True, null=True)  # Field name made lowercase.
    radif = models.IntegerField(db_column='Radif', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'GoodFirstAsset'
        unique_together = (('goodcode', 'storecode', 'tmp'),)


class Goodgrps(models.Model):
    code = models.SmallIntegerField(db_column='Code', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=50, blank=True, null=True)  # Field name made lowercase.
    comment = models.CharField(db_column='Comment', max_length=500, blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return self.name if self.name else f"گروه کد {self.code}"

    class Meta:
        managed = False
        db_table = 'GoodGrps'


class Goodinf(models.Model):
    grpcode = models.ForeignKey(Goodgrps, on_delete=models.DO_NOTHING, db_column='GrpCode')  # Field name made lowercase.
    code = models.IntegerField(db_column='Code', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', unique=True, max_length=153, blank=True, null=True)  # Field name made lowercase.
    abbname = models.CharField(db_column='AbbName', max_length=300, blank=True, null=True)  # Field name made lowercase.
    pos = models.CharField(db_column='Pos', max_length=50, blank=True, null=True)  # Field name made lowercase.
    minava = models.DecimalField(db_column='MinAva', max_digits=23, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    unit = models.ForeignKey('Units', on_delete=models.DO_NOTHING, db_column='Unit')  # Field name made lowercase.
    avabgprd = models.DecimalField(db_column='AvaBgPrd', max_digits=23, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    costbgprd = models.DecimalField(db_column='CostBgPrd', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    curava = models.IntegerField(db_column='CurAva', blank=True, null=True)  # Field name made lowercase.
    status = models.SmallIntegerField(db_column='Status', blank=True, null=True)  # Field name made lowercase.
    mogodi = models.DecimalField(db_column='Mogodi', max_digits=23, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    varede = models.DecimalField(max_digits=23, decimal_places=8, blank=True, null=True)
    sadere = models.DecimalField(max_digits=23, decimal_places=8, blank=True, null=True)
    gheymat_miangin = models.DecimalField(max_digits=23, decimal_places=9, blank=True, null=True)
    unit2 = models.ForeignKey('Units', on_delete=models.DO_NOTHING, db_column='Unit2', related_name='goodinf_unit2_set', blank=True, null=True)  # Field name made lowercase.
    avabgprd2 = models.DecimalField(db_column='AvaBgPrd2', max_digits=23, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    mogodi2 = models.DecimalField(db_column='Mogodi2', max_digits=23, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    meghdar2 = models.DecimalField(db_column='Meghdar2', max_digits=23, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    kala_type = models.CharField(max_length=50, blank=True, null=True)
    kala_index = models.CharField(max_length=50, blank=True, null=True)
    kala_name = models.CharField(max_length=50, blank=True, null=True)
    meghdar_formool = models.DecimalField(db_column='Meghdar_Formool', max_digits=23, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    store = models.ForeignKey('Stores', on_delete=models.DO_NOTHING, db_column='Store')  # Field name made lowercase.
    position = models.CharField(db_column='Position', max_length=50, blank=True, null=True)  # Field name made lowercase.
    smscode = models.CharField(db_column='SMSCode', max_length=50, blank=True, null=True)  # Field name made lowercase.
    offpercent = models.DecimalField(db_column='OffPercent', max_digits=23, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    taxexempt = models.BooleanField(db_column='TaxExempt')  # Field name made lowercase.
    chargeexempt = models.BooleanField(db_column='ChargeExempt')  # Field name made lowercase.
    weight = models.DecimalField(db_column='Weight', max_digits=23, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    length = models.DecimalField(db_column='Length', max_digits=23, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    width = models.DecimalField(db_column='Width', max_digits=23, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    height = models.DecimalField(db_column='Height', max_digits=23, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    stock = models.DecimalField(db_column='Stock', max_digits=23, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    vouchercode = models.IntegerField(db_column='VoucherCode', blank=True, null=True)  # Field name made lowercase.
    groupdiscount = models.SmallIntegerField(db_column='GroupDiscount', blank=True, null=True)  # Field name made lowercase.
    tax_in_sellcosts = models.BooleanField(db_column='Tax_In_SellCosts', blank=True, null=True)  # Field name made lowercase.
    tax_in_buycosts = models.BooleanField(db_column='Tax_In_BuyCosts', blank=True, null=True)  # Field name made lowercase.
    tags = models.CharField(max_length=100, blank=True, null=True)
    comment = models.CharField(db_column='Comment', max_length=500, blank=True, null=True)  # Field name made lowercase.
    createdtime = models.CharField(db_column='CreatedTime', max_length=5, blank=True, null=True)  # Field name made lowercase.
    createddate = models.CharField(db_column='CreatedDate', max_length=10, blank=True, null=True)  # Field name made lowercase.
    modifiedtime = models.CharField(db_column='ModifiedTime', max_length=5, blank=True, null=True)  # Field name made lowercase.
    modifieddate = models.CharField(db_column='ModifiedDate', max_length=10, blank=True, null=True)  # Field name made lowercase.
    usercreated = models.CharField(db_column='UserCreated', max_length=50, blank=True, null=True)  # Field name made lowercase.
    usermodified = models.CharField(db_column='UserModified', max_length=50, blank=True, null=True)  # Field name made lowercase.
    featuresdetail = models.CharField(db_column='FeaturesDetail', max_length=3, blank=True, null=True)  # Field name made lowercase.
    consumerprice = models.DecimalField(db_column='ConsumerPrice', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    daraigoodtype = models.SmallIntegerField(db_column='DaraiGoodType', blank=True, null=True)  # Field name made lowercase.
    taxpercent = models.DecimalField(db_column='TaxPercent', max_digits=23, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    chargepercent = models.DecimalField(db_column='ChargePercent', max_digits=23, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    producttin = models.CharField(db_column='ProductTIN', max_length=50, blank=True, null=True)  # Field name made lowercase.
    electroniccoupongoodsid = models.ForeignKey(Electroniccoupongoods, on_delete=models.DO_NOTHING, db_column='ElectronicCouponGoodsID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'GoodInf'


class GroupPlu(models.Model):
    plu = models.IntegerField(db_column='PLU', primary_key=True)  # Field name made lowercase.
    group1 = models.IntegerField(db_column='Group1', blank=True, null=True)  # Field name made lowercase.
    group2 = models.IntegerField(db_column='Group2', blank=True, null=True)  # Field name made lowercase.
    group3 = models.IntegerField(db_column='Group3', blank=True, null=True)  # Field name made lowercase.
    group4 = models.IntegerField(db_column='Group4', blank=True, null=True)  # Field name made lowercase.
    group5 = models.IntegerField(db_column='Group5', blank=True, null=True)  # Field name made lowercase.
    group6 = models.IntegerField(db_column='Group6', blank=True, null=True)  # Field name made lowercase.
    group7 = models.IntegerField(db_column='Group7', blank=True, null=True)  # Field name made lowercase.
    group8 = models.IntegerField(db_column='Group8', blank=True, null=True)  # Field name made lowercase.
    group9 = models.IntegerField(db_column='Group9', blank=True, null=True)  # Field name made lowercase.
    group10 = models.IntegerField(db_column='Group10', blank=True, null=True)  # Field name made lowercase.
    group11 = models.IntegerField(db_column='Group11', blank=True, null=True)  # Field name made lowercase.
    group12 = models.IntegerField(db_column='Group12', blank=True, null=True)  # Field name made lowercase.
    group13 = models.IntegerField(db_column='Group13', blank=True, null=True)  # Field name made lowercase.
    group14 = models.IntegerField(db_column='Group14', blank=True, null=True)  # Field name made lowercase.
    group15 = models.IntegerField(db_column='Group15', blank=True, null=True)  # Field name made lowercase.
    group16 = models.IntegerField(db_column='Group16', blank=True, null=True)  # Field name made lowercase.
    group17 = models.IntegerField(db_column='Group17', blank=True, null=True)  # Field name made lowercase.
    group18 = models.IntegerField(db_column='Group18', blank=True, null=True)  # Field name made lowercase.
    group19 = models.IntegerField(db_column='Group19', blank=True, null=True)  # Field name made lowercase.
    group20 = models.IntegerField(db_column='Group20', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Group-PLU'


class Groups(models.Model):
    groupname = models.CharField(db_column='GroupName', max_length=25, blank=True, null=True)  # Field name made lowercase.
    groupno = models.IntegerField(db_column='GroupNo', primary_key=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=255, blank=True, null=True)  # Field name made lowercase.
    scale1 = models.CharField(db_column='Scale1', max_length=2, blank=True, null=True)  # Field name made lowercase.
    scale2 = models.CharField(db_column='Scale2', max_length=2, blank=True, null=True)  # Field name made lowercase.
    scale3 = models.CharField(db_column='Scale3', max_length=2, blank=True, null=True)  # Field name made lowercase.
    scale4 = models.CharField(db_column='Scale4', max_length=2, blank=True, null=True)  # Field name made lowercase.
    scale5 = models.CharField(db_column='Scale5', max_length=2, blank=True, null=True)  # Field name made lowercase.
    scale6 = models.CharField(db_column='Scale6', max_length=2, blank=True, null=True)  # Field name made lowercase.
    scale7 = models.CharField(db_column='Scale7', max_length=2, blank=True, null=True)  # Field name made lowercase.
    scale8 = models.CharField(db_column='Scale8', max_length=2, blank=True, null=True)  # Field name made lowercase.
    scale9 = models.CharField(db_column='Scale9', max_length=2, blank=True, null=True)  # Field name made lowercase.
    scale10 = models.CharField(db_column='Scale10', max_length=2, blank=True, null=True)  # Field name made lowercase.
    scale11 = models.CharField(db_column='Scale11', max_length=2, blank=True, null=True)  # Field name made lowercase.
    scale12 = models.CharField(db_column='Scale12', max_length=2, blank=True, null=True)  # Field name made lowercase.
    scale13 = models.CharField(db_column='Scale13', max_length=2, blank=True, null=True)  # Field name made lowercase.
    scale14 = models.CharField(db_column='Scale14', max_length=2, blank=True, null=True)  # Field name made lowercase.
    scale15 = models.CharField(db_column='Scale15', max_length=2, blank=True, null=True)  # Field name made lowercase.
    scale16 = models.CharField(db_column='Scale16', max_length=2, blank=True, null=True)  # Field name made lowercase.
    scale17 = models.CharField(db_column='Scale17', max_length=2, blank=True, null=True)  # Field name made lowercase.
    scale18 = models.CharField(db_column='Scale18', max_length=2, blank=True, null=True)  # Field name made lowercase.
    scale19 = models.CharField(db_column='Scale19', max_length=2, blank=True, null=True)  # Field name made lowercase.
    scale20 = models.CharField(db_column='Scale20', max_length=2, blank=True, null=True)  # Field name made lowercase.
    scale21 = models.CharField(db_column='Scale21', max_length=2, blank=True, null=True)  # Field name made lowercase.
    scale22 = models.CharField(db_column='Scale22', max_length=2, blank=True, null=True)  # Field name made lowercase.
    scale23 = models.CharField(db_column='Scale23', max_length=2, blank=True, null=True)  # Field name made lowercase.
    scale24 = models.CharField(db_column='Scale24', max_length=2, blank=True, null=True)  # Field name made lowercase.
    scale25 = models.CharField(db_column='Scale25', max_length=2, blank=True, null=True)  # Field name made lowercase.
    scale26 = models.CharField(db_column='Scale26', max_length=2, blank=True, null=True)  # Field name made lowercase.
    scale27 = models.CharField(db_column='Scale27', max_length=2, blank=True, null=True)  # Field name made lowercase.
    scale28 = models.CharField(db_column='Scale28', max_length=2, blank=True, null=True)  # Field name made lowercase.
    scale29 = models.CharField(db_column='Scale29', max_length=2, blank=True, null=True)  # Field name made lowercase.
    scale30 = models.CharField(db_column='Scale30', max_length=2, blank=True, null=True)  # Field name made lowercase.
    storecode = models.IntegerField(db_column='StoreCode', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Groups'


class Grpasset(models.Model):
    code = models.IntegerField(db_column='Code', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=50)  # Field name made lowercase.
    comment = models.CharField(db_column='Comment', max_length=500, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'GrpAsset'


class Havaleanbar(models.Model):
    code = models.IntegerField(db_column='Code', primary_key=True)  # Field name made lowercase.
    date = models.CharField(db_column='Date', max_length=10, blank=True, null=True)  # Field name made lowercase.
    comment = models.CharField(db_column='Comment', max_length=500, blank=True, null=True)  # Field name made lowercase.
    com_index = models.IntegerField(db_column='Com_Index')  # Field name made lowercase.
    jam = models.DecimalField(db_column='Jam', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    anbarfrom = models.IntegerField(db_column='AnbarFrom', blank=True, null=True)  # Field name made lowercase.
    anbarto = models.IntegerField(db_column='AnbarTo', blank=True, null=True)  # Field name made lowercase.
    global_field = models.ForeignKey(GlobalIds, on_delete=models.DO_NOTHING, db_column='Global_ID', blank=True, null=True)  # Field name made lowercase. Field renamed because it was a Python reserved word.
    createdtime = models.CharField(db_column='CreatedTime', max_length=5, blank=True, null=True)  # Field name made lowercase.
    createddate = models.CharField(db_column='CreatedDate', max_length=10, blank=True, null=True)  # Field name made lowercase.
    modifiedtime = models.CharField(db_column='ModifiedTime', max_length=5, blank=True, null=True)  # Field name made lowercase.
    modifieddate = models.CharField(db_column='ModifiedDate', max_length=10, blank=True, null=True)  # Field name made lowercase.
    usercreated = models.IntegerField(db_column='UserCreated')  # Field name made lowercase.
    usermodified = models.IntegerField(db_column='UserModified', blank=True, null=True)  # Field name made lowercase.
    owner = models.IntegerField(db_column='Owner')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'HavaleAnbar'


class HavaleanbarDetail(models.Model):
    code = models.IntegerField(db_column='Code', blank=True, null=True)  # Field name made lowercase.
    radif = models.IntegerField(db_column='Radif', blank=True, null=True)  # Field name made lowercase.
    com_index = models.IntegerField(db_column='Com_Index')  # Field name made lowercase.
    temp = models.SmallIntegerField(db_column='Temp', blank=True, null=True)  # Field name made lowercase.
    kalacode = models.IntegerField(db_column='KalaCode', blank=True, null=True)  # Field name made lowercase.
    meghdar = models.DecimalField(db_column='Meghdar', max_digits=23, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    meghdar2 = models.DecimalField(db_column='Meghdar2', max_digits=23, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    tool = models.DecimalField(db_column='Tool', max_digits=23, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    arz = models.DecimalField(db_column='Arz', max_digits=23, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    mablagh = models.DecimalField(db_column='Mablagh', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    comment = models.CharField(db_column='Comment', max_length=500, blank=True, null=True)  # Field name made lowercase.
    tedad = models.DecimalField(db_column='Tedad', max_digits=23, decimal_places=8, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'HavaleAnbar_Detail'
        unique_together = (('code', 'radif', 'temp'),)


class HavaleHesab(models.Model):
    date = models.CharField(db_column='Date', max_length=10, blank=True, null=True)  # Field name made lowercase.
    comment = models.CharField(db_column='Comment', max_length=500, blank=True, null=True)  # Field name made lowercase.
    amount = models.DecimalField(db_column='Amount', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    bed = models.SmallIntegerField(db_column='Bed', blank=True, null=True)  # Field name made lowercase.
    bes = models.SmallIntegerField(db_column='Bes', blank=True, null=True)  # Field name made lowercase.
    bedcode = models.IntegerField(db_column='BedCode', blank=True, null=True)  # Field name made lowercase.
    bescode = models.IntegerField(db_column='BesCode', blank=True, null=True)  # Field name made lowercase.
    code = models.IntegerField(db_column='Code', primary_key=True)  # Field name made lowercase.
    vouchercode = models.IntegerField(db_column='VoucherCode', blank=True, null=True)  # Field name made lowercase.
    expcentercode = models.IntegerField(db_column='ExpCenterCode', blank=True, null=True)  # Field name made lowercase.
    currcode = models.IntegerField(db_column='CurrCode', blank=True, null=True)  # Field name made lowercase.
    currrate = models.DecimalField(db_column='CurrRate', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    createdtime = models.CharField(db_column='CreatedTime', max_length=5, blank=True, null=True)  # Field name made lowercase.
    createddate = models.CharField(db_column='CreatedDate', max_length=10, blank=True, null=True)  # Field name made lowercase.
    modifiedtime = models.CharField(db_column='ModifiedTime', max_length=5, blank=True, null=True)  # Field name made lowercase.
    modifieddate = models.CharField(db_column='ModifiedDate', max_length=10, blank=True, null=True)  # Field name made lowercase.
    usercreated = models.IntegerField(db_column='UserCreated')  # Field name made lowercase.
    usermodified = models.IntegerField(db_column='UserModified', blank=True, null=True)  # Field name made lowercase.
    bankwagecode = models.IntegerField(db_column='BankWageCode', blank=True, null=True)  # Field name made lowercase.
    bankwagecost = models.DecimalField(db_column='BankWageCost', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    global_id = models.IntegerField(db_column='Global_ID', blank=True, null=True)  # Field name made lowercase.
    owner = models.IntegerField(db_column='Owner')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Havale_Hesab'


class IsAnalyticresult(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    analyticid = models.ForeignKey('IsAnalytics', on_delete=models.DO_NOTHING, db_column='AnalyticID', blank=True, null=True)  # Field name made lowercase.
    regdate = models.DateTimeField(db_column='RegDate', blank=True, null=True)  # Field name made lowercase.
    issent = models.BooleanField(db_column='IsSent', blank=True, null=True)  # Field name made lowercase.
    field1 = models.CharField(db_column='Field1', max_length=50, blank=True, null=True)  # Field name made lowercase.
    field2 = models.CharField(db_column='Field2', max_length=50, blank=True, null=True)  # Field name made lowercase.
    field3 = models.CharField(db_column='Field3', max_length=50, blank=True, null=True)  # Field name made lowercase.
    field4 = models.CharField(db_column='Field4', max_length=50, blank=True, null=True)  # Field name made lowercase.
    field5 = models.CharField(db_column='Field5', max_length=50, blank=True, null=True)  # Field name made lowercase.
    priod = models.IntegerField(db_column='Priod', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'IS_AnalyticResult'


class IsAnalytics(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    subject = models.CharField(db_column='Subject', max_length=100, blank=True, null=True)  # Field name made lowercase.
    tsql = models.TextField(db_column='TSQL', blank=True, null=True)  # Field name made lowercase.
    lastrundate = models.DateTimeField(db_column='LastRunDate', blank=True, null=True)  # Field name made lowercase.
    startdate = models.DateTimeField(db_column='StartDate', blank=True, null=True)  # Field name made lowercase.
    expiredate = models.DateTimeField(db_column='ExpireDate', blank=True, null=True)  # Field name made lowercase.
    maxperiod = models.IntegerField(db_column='MaxPeriod', blank=True, null=True)  # Field name made lowercase.
    status = models.SmallIntegerField(db_column='Status', blank=True, null=True)  # Field name made lowercase.
    period = models.IntegerField(db_column='Period', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'IS_Analytics'


class IsContractinfo(models.Model):
    fullname = models.CharField(db_column='FullName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    brithdate = models.CharField(db_column='BrithDate', max_length=10, blank=True, null=True)  # Field name made lowercase.
    expiredate = models.DateTimeField(db_column='ExpireDate', blank=True, null=True)  # Field name made lowercase.
    notifyday = models.SmallIntegerField(db_column='NotifyDay', blank=True, null=True)  # Field name made lowercase.
    brithdatemessage = models.CharField(db_column='BrithDateMessage', max_length=200, blank=True, null=True)  # Field name made lowercase.
    expiredatemessage = models.CharField(db_column='ExpireDateMessage', max_length=200, blank=True, null=True)  # Field name made lowercase.
    expiredatemessage1 = models.CharField(db_column='ExpireDateMessage1', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'IS_ContractInfo'


class IsMessages(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    subject = models.CharField(db_column='Subject', max_length=200, blank=True, null=True)  # Field name made lowercase.
    url = models.CharField(db_column='URL', max_length=200, blank=True, null=True)  # Field name made lowercase.
    startdate = models.DateTimeField(db_column='StartDate', blank=True, null=True)  # Field name made lowercase.
    expiredate = models.DateTimeField(db_column='ExpireDate', blank=True, null=True)  # Field name made lowercase.
    lastreaddate = models.DateTimeField(db_column='LastReadDate', blank=True, null=True)  # Field name made lowercase.
    lastnotifydate = models.DateTimeField(db_column='LastNotifyDate', blank=True, null=True)  # Field name made lowercase.
    periodtime = models.SmallIntegerField(db_column='PeriodTime', blank=True, null=True)  # Field name made lowercase.
    status = models.SmallIntegerField(db_column='Status', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'IS_Messages'


class IsPoll(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    subject = models.CharField(db_column='Subject', max_length=200, blank=True, null=True)  # Field name made lowercase.
    kind = models.SmallIntegerField(db_column='Kind', blank=True, null=True)  # Field name made lowercase.
    switchcount = models.SmallIntegerField(db_column='SwitchCount', blank=True, null=True)  # Field name made lowercase.
    startdate = models.DateTimeField(db_column='StartDate', blank=True, null=True)  # Field name made lowercase.
    expiredate = models.DateTimeField(db_column='ExpireDate', blank=True, null=True)  # Field name made lowercase.
    showcount = models.SmallIntegerField(db_column='ShowCount', blank=True, null=True)  # Field name made lowercase.
    periodtime = models.SmallIntegerField(db_column='PeriodTime', blank=True, null=True)  # Field name made lowercase.
    status = models.SmallIntegerField(db_column='Status', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'IS_Poll'


class IsPollanswer(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    pollid = models.IntegerField(db_column='PollID', blank=True, null=True)  # Field name made lowercase.
    pollswitchid = models.IntegerField(db_column='PollSwitchID', blank=True, null=True)  # Field name made lowercase.
    comment = models.CharField(db_column='Comment', max_length=250, blank=True, null=True)  # Field name made lowercase.
    username = models.CharField(db_column='UserName', max_length=200, blank=True, null=True)  # Field name made lowercase.
    issent = models.BooleanField(db_column='IsSent', blank=True, null=True)  # Field name made lowercase.
    istmp = models.BooleanField(db_column='IsTmp', blank=True, null=True)  # Field name made lowercase.
    regdate = models.DateTimeField(db_column='RegDate', blank=True, null=True)  # Field name made lowercase.
    priod = models.IntegerField(db_column='Priod', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'IS_PollAnswer'


class IsPollswitch(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    pollid = models.IntegerField(db_column='PollID', blank=True, null=True)  # Field name made lowercase.
    answertext = models.CharField(db_column='AnswerText', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'IS_PollSwitch'


class Itemtype(models.Model):
    itemtype = models.IntegerField(db_column='ItemType', primary_key=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ItemType'


class Items(models.Model):
    id = models.IntegerField(db_column='ID', blank=True, null=True)  # Field name made lowercase.
    code = models.IntegerField(db_column='Code', primary_key=True)  # Field name made lowercase.
    name1 = models.CharField(max_length=50, blank=True, null=True)
    name2 = models.CharField(max_length=20, blank=True, null=True)
    barcode = models.CharField(db_column='BarCode', max_length=30, blank=True, null=True)  # Field name made lowercase.
    irancode = models.CharField(db_column='IranCode', max_length=16, blank=True, null=True)  # Field name made lowercase.
    type = models.IntegerField(db_column='Type', blank=True, null=True)  # Field name made lowercase.
    price = models.IntegerField(db_column='Price', blank=True, null=True)  # Field name made lowercase.
    itemcode = models.IntegerField(db_column='ItemCode', blank=True, null=True)  # Field name made lowercase.
    alterprice = models.IntegerField(db_column='AlterPrice', blank=True, null=True)  # Field name made lowercase.
    sect = models.IntegerField(db_column='Sect', blank=True, null=True)  # Field name made lowercase.
    costlevel_type = models.IntegerField(db_column='costlevel_Type', blank=True, null=True)  # Field name made lowercase.
    scaletype = models.SmallIntegerField(db_column='ScaleType', blank=True, null=True)  # Field name made lowercase.
    changetype = models.SmallIntegerField(db_column='ChangeType', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Items'


class KalaHazine(models.Model):
    hazine_code = models.IntegerField(db_column='Hazine_Code', blank=True, null=True)  # Field name made lowercase.
    date = models.CharField(db_column='Date', max_length=10, blank=True, null=True)  # Field name made lowercase.
    jam = models.DecimalField(db_column='Jam', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    comment = models.CharField(db_column='Comment', max_length=500, blank=True, null=True)  # Field name made lowercase.
    code = models.IntegerField(db_column='Code', primary_key=True)  # Field name made lowercase.
    vouchercode = models.IntegerField(db_column='VoucherCode', blank=True, null=True)  # Field name made lowercase.
    expcentercode = models.IntegerField(db_column='ExpCenterCode', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Kala_Hazine'


class KalaHazineDetail(models.Model):
    kala_code = models.IntegerField(db_column='Kala_Code', blank=True, null=True)  # Field name made lowercase.
    meghdar = models.DecimalField(db_column='Meghdar', max_digits=23, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    gheymat = models.DecimalField(db_column='Gheymat', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    code = models.IntegerField(db_column='Code')  # Field name made lowercase.
    tool = models.DecimalField(db_column='Tool', max_digits=23, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    arz = models.DecimalField(db_column='Arz', max_digits=23, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    tedad = models.DecimalField(db_column='Tedad', max_digits=23, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    anbar = models.IntegerField(db_column='Anbar', blank=True, null=True)  # Field name made lowercase.
    meghdar2 = models.DecimalField(db_column='Meghdar2', max_digits=23, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    radif = models.SmallIntegerField(db_column='Radif', blank=True, null=True)  # Field name made lowercase.
    comment = models.CharField(db_column='Comment', max_length=500, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Kala_Hazine_Detail'


class KalaCategory(models.Model):
    id = id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    kala_code = models.IntegerField(db_column='Kala_code')  # Field name made lowercase.
    category_code = models.IntegerField(db_column='Category_code')  # Field name made lowercase.
    tmp = models.IntegerField(db_column='Tmp')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Kala_category'


class Kardex(models.Model):
    date = models.CharField(db_column='Date', max_length=12, blank=True, null=True)  # Field name made lowercase.
    percode = models.IntegerField(db_column='PerCode', blank=True, null=True)  # Field name made lowercase.
    anbar = models.IntegerField(db_column='Anbar', blank=True, null=True)  # Field name made lowercase.
    amount = models.DecimalField(db_column='Amount', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    kala = models.IntegerField(db_column='Kala', blank=True, null=True)  # Field name made lowercase.
    type = models.SmallIntegerField(db_column='Type', blank=True, null=True)  # Field name made lowercase.
    code = models.CharField(db_column='Code', max_length=50, blank=True, null=True)  # Field name made lowercase.
    tedad = models.DecimalField(db_column='Tedad', max_digits=23, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    sanad_code = models.IntegerField(db_column='Sanad_Code', blank=True, null=True)  # Field name made lowercase.
    amount2 = models.DecimalField(db_column='Amount2', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    tedad2 = models.DecimalField(db_column='Tedad2', max_digits=23, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    miangin = models.DecimalField(db_column='Miangin', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    bagh = models.DecimalField(db_column='Bagh', max_digits=23, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    status = models.SmallIntegerField(db_column='Status', blank=True, null=True)  # Field name made lowercase.
    radif = models.BigAutoField(db_column='Radif', primary_key=True)  # Field name made lowercase.
    bagh2 = models.DecimalField(db_column='Bagh2', max_digits=23, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    remaininanbar = models.DecimalField(db_column='RemainInAnbar', max_digits=23, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    statusinanbar = models.SmallIntegerField(db_column='StatusInAnbar', blank=True, null=True)  # Field name made lowercase.
    transfercode = models.IntegerField(db_column='TransferCode', blank=True, null=True)  # Field name made lowercase.
    global_field = models.ForeignKey(GlobalIds, on_delete=models.DO_NOTHING, db_column='Global_ID', blank=True, null=True)  # Field name made lowercase. Field renamed because it was a Python reserved word.
    prioritytype = models.SmallIntegerField(db_column='PriorityType')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Kardex'
        unique_together = (('kala', 'type', 'code', 'sanad_code'),)


class KarmozdBank(models.Model):
    bank_code = models.IntegerField(db_column='Bank_Code', blank=True, null=True)  # Field name made lowercase.
    date = models.CharField(db_column='Date', max_length=10, blank=True, null=True)  # Field name made lowercase.
    amount = models.DecimalField(db_column='Amount', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    comment = models.CharField(db_column='Comment', max_length=500, blank=True, null=True)  # Field name made lowercase.
    code = models.IntegerField(db_column='cODE')  # Field name made lowercase.
    vouchercode = models.IntegerField(db_column='VoucherCode', blank=True, null=True)  # Field name made lowercase.
    expcentercode = models.IntegerField(db_column='ExpCenterCode', blank=True, null=True)  # Field name made lowercase.
    operationtype = models.SmallIntegerField(db_column='OperationType', blank=True, null=True)  # Field name made lowercase.
    global_id = models.IntegerField(db_column='Global_ID', blank=True, null=True)  # Field name made lowercase.
    currcode = models.IntegerField(db_column='CurrCode')  # Field name made lowercase.
    currrate = models.DecimalField(db_column='CurrRate', max_digits=23, decimal_places=9)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Karmozd_Bank'


class Keyinf(models.Model):
    code = models.IntegerField(db_column='Code')  # Field name made lowercase.
    tabcode = models.IntegerField(db_column='TabCode')  # Field name made lowercase.
    goodcode = models.IntegerField(db_column='GoodCode')  # Field name made lowercase.
    iconindex = models.IntegerField(db_column='IconIndex', blank=True, null=True)  # Field name made lowercase.
    managetype = models.SmallIntegerField(db_column='ManageType', blank=True, null=True)  # Field name made lowercase.
    usercode = models.IntegerField(db_column='UserCode', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'KeyInf'


class Kharid(models.Model):
    code = models.IntegerField(primary_key=True)
    shakhs_code = models.ForeignKey('Perinf', on_delete=models.DO_NOTHING, db_column='shakhs_code')
    tarikh = models.CharField(max_length=10)
    mablagh_factor = models.DecimalField(max_digits=23, decimal_places=9, blank=True, null=True)
    takhfif = models.DecimalField(max_digits=23, decimal_places=9, blank=True, null=True)
    sanad_code = models.IntegerField(blank=True, null=True)
    sharh = models.CharField(max_length=500, blank=True, null=True)
    status = models.SmallIntegerField(db_column='Status', blank=True, null=True)  # Field name made lowercase.
    sanad = models.IntegerField(db_column='Sanad', blank=True, null=True)  # Field name made lowercase.
    tarikhvosoul = models.CharField(max_length=10, blank=True, null=True)
    tasviye = models.SmallIntegerField(blank=True, null=True)
    com_index = models.IntegerField()
    charge = models.DecimalField(db_column='Charge', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    tax = models.DecimalField(db_column='Tax', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    expcentercode = models.IntegerField(db_column='ExpCenterCode', blank=True, null=True)  # Field name made lowercase.
    refrenceid = models.CharField(db_column='RefrenceID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    currcode = models.IntegerField(db_column='CurrCode', blank=True, null=True)  # Field name made lowercase.
    currrate = models.DecimalField(db_column='CurrRate', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    global_field = models.ForeignKey(GlobalIds, on_delete=models.DO_NOTHING, db_column='Global_ID', blank=True, null=True)  # Field name made lowercase. Field renamed because it was a Python reserved word.
    createdtime = models.CharField(db_column='CreatedTime', max_length=5, blank=True, null=True)  # Field name made lowercase.
    createddate = models.CharField(db_column='CreatedDate', max_length=10, blank=True, null=True)  # Field name made lowercase.
    modifiedtime = models.CharField(db_column='ModifiedTime', max_length=5, blank=True, null=True)  # Field name made lowercase.
    modifieddate = models.CharField(db_column='ModifiedDate', max_length=10, blank=True, null=True)  # Field name made lowercase.
    usercreated = models.IntegerField(db_column='UserCreated')  # Field name made lowercase.
    usermodified = models.IntegerField(db_column='UserModified', blank=True, null=True)  # Field name made lowercase.
    takhfif_type = models.BooleanField(db_column='Takhfif_Type', blank=True, null=True)  # Field name made lowercase.
    takhfif_percent = models.DecimalField(db_column='Takhfif_Percent', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    owner = models.IntegerField(db_column='Owner')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Kharid'


class Ldaramad(models.Model):
    code = models.IntegerField(db_column='Code', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=100, blank=True, null=True)  # Field name made lowercase.
    gcode = models.SmallIntegerField(db_column='GCode', blank=True, null=True)  # Field name made lowercase.
    comment = models.CharField(db_column='Comment', max_length=500, blank=True, null=True)  # Field name made lowercase.
    amount = models.DecimalField(db_column='Amount', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    createdtime = models.CharField(db_column='CreatedTime', max_length=5, blank=True, null=True)  # Field name made lowercase.
    createddate = models.CharField(db_column='CreatedDate', max_length=10, blank=True, null=True)  # Field name made lowercase.
    modifiedtime = models.CharField(db_column='ModifiedTime', max_length=5, blank=True, null=True)  # Field name made lowercase.
    modifieddate = models.CharField(db_column='ModifiedDate', max_length=10, blank=True, null=True)  # Field name made lowercase.
    usercreated = models.CharField(db_column='UserCreated', max_length=50, blank=True, null=True)  # Field name made lowercase.
    usermodified = models.CharField(db_column='UserModified', max_length=50, blank=True, null=True)  # Field name made lowercase.
    defaultcost = models.DecimalField(db_column='DefaultCost', max_digits=23, decimal_places=9)  # Field name made lowercase.
    incometin = models.CharField(db_column='IncomeTIN', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LDaramad'


class LHazine(models.Model):
    code = models.IntegerField(db_column='Code', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=100, blank=True, null=True)  # Field name made lowercase.
    comment = models.CharField(db_column='Comment', max_length=500, blank=True, null=True)  # Field name made lowercase.
    g_code = models.IntegerField(db_column='G_Code', blank=True, null=True)  # Field name made lowercase.
    amount = models.DecimalField(db_column='Amount', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    createdtime = models.CharField(db_column='CreatedTime', max_length=5, blank=True, null=True)  # Field name made lowercase.
    createddate = models.CharField(db_column='CreatedDate', max_length=10, blank=True, null=True)  # Field name made lowercase.
    modifiedtime = models.CharField(db_column='ModifiedTime', max_length=5, blank=True, null=True)  # Field name made lowercase.
    modifieddate = models.CharField(db_column='ModifiedDate', max_length=10, blank=True, null=True)  # Field name made lowercase.
    usercreated = models.CharField(db_column='UserCreated', max_length=50, blank=True, null=True)  # Field name made lowercase.
    usermodified = models.CharField(db_column='UserModified', max_length=50, blank=True, null=True)  # Field name made lowercase.
    defaultcost = models.DecimalField(db_column='DefaultCost', max_digits=23, decimal_places=9)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'L_Hazine'


class Languages(models.Model):
    code = models.SmallIntegerField(db_column='Code', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=50)  # Field name made lowercase.
    symbol = models.CharField(db_column='Symbol', max_length=10)  # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Languages'


class Letter(models.Model):
    code = models.IntegerField(db_column='Code', primary_key=True)  # Field name made lowercase.
    andicatorcode = models.CharField(db_column='AndicatorCode', max_length=15, blank=True, null=True)  # Field name made lowercase.
    type = models.BooleanField(db_column='Type', blank=True, null=True)  # Field name made lowercase.
    date = models.CharField(db_column='Date', max_length=10)  # Field name made lowercase.
    person = models.CharField(db_column='Person', max_length=50)  # Field name made lowercase.
    refrence = models.CharField(db_column='Refrence', max_length=15, blank=True, null=True)  # Field name made lowercase.
    follow = models.CharField(db_column='Follow', max_length=15, blank=True, null=True)  # Field name made lowercase.
    nahve = models.SmallIntegerField(db_column='Nahve')  # Field name made lowercase.
    classification = models.SmallIntegerField(db_column='Classification')  # Field name made lowercase.
    priority = models.SmallIntegerField(db_column='Priority')  # Field name made lowercase.
    subject = models.CharField(db_column='Subject', max_length=100)  # Field name made lowercase.
    keyword = models.CharField(db_column='KeyWord', max_length=150, blank=True, null=True)  # Field name made lowercase.
    attachment = models.CharField(db_column='Attachment', max_length=100, blank=True, null=True)  # Field name made lowercase.
    grpcode = models.IntegerField(db_column='GrpCode')  # Field name made lowercase.
    usermodified = models.IntegerField(db_column='UserModified', blank=True, null=True)  # Field name made lowercase.
    modifieddate = models.CharField(db_column='ModifiedDate', max_length=10, blank=True, null=True)  # Field name made lowercase.
    modifiedtime = models.CharField(db_column='ModifiedTime', max_length=5, blank=True, null=True)  # Field name made lowercase.
    usercreated = models.IntegerField(db_column='UserCreated')  # Field name made lowercase.
    createdtime = models.CharField(db_column='CreatedTime', max_length=5)  # Field name made lowercase.
    createddate = models.CharField(db_column='CreatedDate', max_length=10)  # Field name made lowercase.
    owner = models.IntegerField(db_column='Owner')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Letter'


class Letterdetail(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    lettercode = models.ForeignKey(Letter, on_delete=models.DO_NOTHING, db_column='LetterCode')  # Field name made lowercase.
    person = models.CharField(db_column='Person', max_length=50)  # Field name made lowercase.
    referplace = models.CharField(db_column='ReferPlace', max_length=50, blank=True, null=True)  # Field name made lowercase.
    dodate = models.CharField(db_column='DoDate', max_length=10, blank=True, null=True)  # Field name made lowercase.
    docomment = models.CharField(db_column='DoComment', max_length=500, blank=True, null=True)  # Field name made lowercase.
    refercomment = models.CharField(db_column='ReferComment', max_length=500, blank=True, null=True)  # Field name made lowercase.
    referuserid = models.IntegerField(db_column='ReferUserId')  # Field name made lowercase.
    referdate = models.CharField(db_column='ReferDate', max_length=10)  # Field name made lowercase.
    refertime = models.CharField(db_column='ReferTime', max_length=5)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LetterDetail'


class Lettergroup(models.Model):
    code = models.IntegerField(db_column='Code', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=50, blank=True, null=True)  # Field name made lowercase.
    comment = models.CharField(db_column='Comment', max_length=500, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LetterGroup'


class Loan(models.Model):
    code = models.IntegerField(db_column='Code', primary_key=True)  # Field name made lowercase. The composite primary key (Code, LoanType) found, that is not supported. The first column is selected.
    nametype = models.BooleanField(db_column='NameType')  # Field name made lowercase.
    namecode = models.IntegerField(db_column='NameCode')  # Field name made lowercase.
    date = models.CharField(db_column='Date', max_length=10)  # Field name made lowercase.
    number = models.SmallIntegerField(db_column='Number')  # Field name made lowercase.
    distance = models.IntegerField(db_column='Distance')  # Field name made lowercase.
    loantype = models.SmallIntegerField(db_column='LoanType')  # Field name made lowercase.
    type = models.SmallIntegerField(db_column='Type')  # Field name made lowercase.
    benefittype = models.SmallIntegerField(db_column='BenefitType', blank=True, null=True)  # Field name made lowercase.
    benefitpercent = models.DecimalField(db_column='BenefitPercent', max_digits=23, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    wage = models.DecimalField(db_column='Wage', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    benefit = models.DecimalField(db_column='Benefit', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    cost = models.DecimalField(db_column='Cost', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=50, blank=True, null=True)  # Field name made lowercase.
    family = models.CharField(db_column='Family', max_length=50, blank=True, null=True)  # Field name made lowercase.
    fathername = models.CharField(db_column='FatherName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    idnumber = models.CharField(db_column='IdNumber', max_length=50, blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=300, blank=True, null=True)  # Field name made lowercase.
    tel = models.CharField(db_column='Tel', max_length=11, blank=True, null=True)  # Field name made lowercase.
    validnum = models.CharField(db_column='ValidNum', max_length=50, blank=True, null=True)  # Field name made lowercase.
    comment = models.CharField(db_column='Comment', max_length=500, blank=True, null=True)  # Field name made lowercase.
    incomecode = models.IntegerField(db_column='IncomeCode', blank=True, null=True)  # Field name made lowercase.
    vouchercode = models.IntegerField(db_column='VoucherCode', blank=True, null=True)  # Field name made lowercase.
    createdtime = models.CharField(db_column='CreatedTime', max_length=5, blank=True, null=True)  # Field name made lowercase.
    createddate = models.CharField(db_column='CreatedDate', max_length=10, blank=True, null=True)  # Field name made lowercase.
    modifiedtime = models.CharField(db_column='ModifiedTime', max_length=5, blank=True, null=True)  # Field name made lowercase.
    modifieddate = models.CharField(db_column='ModifiedDate', max_length=10, blank=True, null=True)  # Field name made lowercase.
    usercreated = models.IntegerField(db_column='UserCreated')  # Field name made lowercase.
    usermodified = models.IntegerField(db_column='UserModified', blank=True, null=True)  # Field name made lowercase.
    lastprcentjarimeh = models.SmallIntegerField(db_column='LastPrcentJarimeh', blank=True, null=True)  # Field name made lowercase.
    owner = models.IntegerField(db_column='Owner')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Loan'
        unique_together = (('code', 'loantype'),)


class Loandetail(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    loancode = models.IntegerField(db_column='LoanCode')  # Field name made lowercase.
    type = models.IntegerField(db_column='Type')  # Field name made lowercase.
    row = models.IntegerField(db_column='Row')  # Field name made lowercase.
    date = models.CharField(db_column='Date', max_length=10)  # Field name made lowercase.
    recievedate = models.CharField(db_column='RecieveDate', max_length=10, blank=True, null=True)  # Field name made lowercase.
    delay = models.DecimalField(db_column='Delay', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    cost = models.DecimalField(db_column='Cost', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    sanadcode = models.IntegerField(db_column='SanadCode')  # Field name made lowercase.
    comment = models.CharField(db_column='Comment', max_length=500, blank=True, null=True)  # Field name made lowercase.
    vouchercode = models.IntegerField(db_column='VoucherCode', blank=True, null=True)  # Field name made lowercase.
    sanadcodetype = models.BooleanField(db_column='SanadCodeType')  # Field name made lowercase.
    paytype = models.SmallIntegerField(db_column='payType', blank=True, null=True)  # Field name made lowercase.
    prcentjarimeh = models.SmallIntegerField(db_column='PrcentJarimeh', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LoanDetail'


class Mahakpaylinks(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    factorcode = models.IntegerField(db_column='FactorCode', blank=True, null=True)  # Field name made lowercase.
    personcode = models.IntegerField(db_column='PersonCode', blank=True, null=True)  # Field name made lowercase.
    paylink = models.CharField(db_column='PayLink', max_length=100, blank=True, null=True)  # Field name made lowercase.
    ispayed = models.IntegerField(db_column='IsPayed', blank=True, null=True)  # Field name made lowercase.
    payableamount = models.DecimalField(db_column='PayableAmount', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    orderid = models.CharField(db_column='OrderId', max_length=100, blank=True, null=True)  # Field name made lowercase.
    apikey = models.CharField(db_column='ApiKey', max_length=100, blank=True, null=True)  # Field name made lowercase.
    assignmentid = models.IntegerField(db_column='AssignmentId', blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=200, blank=True, null=True)  # Field name made lowercase.
    assignmentnumber = models.CharField(db_column='AssignmentNumber', max_length=50, blank=True, null=True)  # Field name made lowercase.
    payername = models.CharField(db_column='PayerName', max_length=171, blank=True, null=True)  # Field name made lowercase.
    payerphone = models.CharField(db_column='PayerPhone', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MahakPayLinks'


class Member(models.Model):
    code = models.IntegerField(db_column='Code', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=50, blank=True, null=True)  # Field name made lowercase.
    family = models.CharField(db_column='Family', max_length=50, blank=True, null=True)  # Field name made lowercase.
    fathername = models.CharField(db_column='FatherName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    nationalid = models.CharField(db_column='NationalId', max_length=20, blank=True, null=True)  # Field name made lowercase.
    idnum = models.CharField(db_column='IdNum', max_length=20, blank=True, null=True)  # Field name made lowercase.
    birthdate = models.CharField(db_column='BirthDate', max_length=10, blank=True, null=True)  # Field name made lowercase.
    export = models.CharField(db_column='Export', max_length=50, blank=True, null=True)  # Field name made lowercase.
    marriage = models.BooleanField(db_column='Marriage', blank=True, null=True)  # Field name made lowercase.
    creditdate = models.CharField(db_column='CreditDate', max_length=10, blank=True, null=True)  # Field name made lowercase.
    pic = models.BinaryField(db_column='Pic', blank=True, null=True)  # Field name made lowercase.
    signpic = models.BinaryField(db_column='SignPic', blank=True, null=True)  # Field name made lowercase.
    comment = models.CharField(db_column='Comment', max_length=250, blank=True, null=True)  # Field name made lowercase.
    grpcode = models.ForeignKey('Membergroup', on_delete=models.DO_NOTHING, db_column='GrpCode')  # Field name made lowercase.
    sex = models.BooleanField(db_column='Sex', blank=True, null=True)  # Field name made lowercase.
    perinfcode = models.ForeignKey('Perinf', on_delete=models.DO_NOTHING, db_column='PerInfCode', blank=True, null=True)  # Field name made lowercase.
    createdtime = models.CharField(db_column='CreatedTime', max_length=5)  # Field name made lowercase.
    createddate = models.CharField(db_column='CreatedDate', max_length=10)  # Field name made lowercase.
    modifiedtime = models.CharField(db_column='ModifiedTime', max_length=5, blank=True, null=True)  # Field name made lowercase.
    modifieddate = models.CharField(db_column='ModifiedDate', max_length=10, blank=True, null=True)  # Field name made lowercase.
    usercreated = models.IntegerField(db_column='UserCreated')  # Field name made lowercase.
    usermodified = models.IntegerField(db_column='UserModified', blank=True, null=True)  # Field name made lowercase.
    owner = models.IntegerField(db_column='Owner')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Member'


class Memberfamily(models.Model):
    code = models.IntegerField(db_column='Code', primary_key=True)  # Field name made lowercase.
    membercode = models.ForeignKey(Member, on_delete=models.DO_NOTHING, db_column='MemberCode')  # Field name made lowercase.
    type = models.BooleanField(db_column='Type', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=100, blank=True, null=True)  # Field name made lowercase.
    sex = models.BooleanField(db_column='Sex', blank=True, null=True)  # Field name made lowercase.
    fathername = models.CharField(db_column='FatherName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    birthdate = models.CharField(db_column='BirthDate', max_length=10, blank=True, null=True)  # Field name made lowercase.
    idnum = models.CharField(db_column='IDNum', max_length=20, blank=True, null=True)  # Field name made lowercase.
    nationalid = models.CharField(db_column='NationalID', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MemberFamily'


class Membergroup(models.Model):
    code = models.IntegerField(db_column='Code', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=50)  # Field name made lowercase.
    comment = models.CharField(db_column='Comment', max_length=500)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MemberGroup'


class Memberpersonal(models.Model):
    membercode = models.ForeignKey(Member, on_delete=models.DO_NOTHING, db_column='MemberCode')  # Field name made lowercase.
    postcode = models.CharField(db_column='PostCode', max_length=20, blank=True, null=True)  # Field name made lowercase.
    nationality = models.CharField(db_column='Nationality', max_length=50, blank=True, null=True)  # Field name made lowercase.
    degree = models.SmallIntegerField(db_column='Degree', blank=True, null=True)  # Field name made lowercase.
    hometel = models.CharField(db_column='HomeTel', max_length=50, blank=True, null=True)  # Field name made lowercase.
    mobile = models.CharField(db_column='Mobile', max_length=50, blank=True, null=True)  # Field name made lowercase.
    fax = models.CharField(db_column='Fax', max_length=50, blank=True, null=True)  # Field name made lowercase.
    homeaddr = models.CharField(db_column='HomeAddr', max_length=200, blank=True, null=True)  # Field name made lowercase.
    coname = models.CharField(db_column='CoName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    profession = models.CharField(db_column='Profession', max_length=50, blank=True, null=True)  # Field name made lowercase.
    precedence = models.CharField(db_column='Precedence', max_length=50, blank=True, null=True)  # Field name made lowercase.
    type = models.SmallIntegerField(db_column='Type', blank=True, null=True)  # Field name made lowercase.
    personnelcount = models.IntegerField(db_column='PersonnelCount', blank=True, null=True)  # Field name made lowercase.
    insurancecount = models.IntegerField(db_column='InsuranceCount', blank=True, null=True)  # Field name made lowercase.
    workaddr = models.CharField(db_column='WorkAddr', max_length=200, blank=True, null=True)  # Field name made lowercase.
    worktel = models.CharField(db_column='WorkTel', max_length=50, blank=True, null=True)  # Field name made lowercase.
    etehadiyenu = models.CharField(db_column='EtehadiyeNu', max_length=50, blank=True, null=True)  # Field name made lowercase.
    parvanenu = models.CharField(db_column='ParvaneNu', max_length=50, blank=True, null=True)  # Field name made lowercase.
    accountnu = models.CharField(db_column='AccountNu', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MemberPersonal'


class Mes(models.Model):
    code = models.IntegerField(db_column='Code', primary_key=True)  # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=300)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Mes'


class Message(models.Model):
    code = models.IntegerField(db_column='Code', primary_key=True)  # Field name made lowercase.
    enumtitle = models.CharField(db_column='EnumTitle', unique=True, max_length=50)  # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=50, blank=True, null=True)  # Field name made lowercase.
    message = models.CharField(db_column='Message', max_length=500, blank=True, null=True)  # Field name made lowercase.
    buttons = models.SmallIntegerField(db_column='Buttons')  # Field name made lowercase.
    reason = models.CharField(db_column='Reason', max_length=500, blank=True, null=True)  # Field name made lowercase.
    showtype = models.SmallIntegerField(db_column='ShowType')  # Field name made lowercase.
    softwarepartcode = models.ForeignKey('Softwarepart', on_delete=models.DO_NOTHING, db_column='SoftwarePartCode')  # Field name made lowercase.
    helpcontext = models.IntegerField(db_column='HelpContext')  # Field name made lowercase.
    remember = models.SmallIntegerField(db_column='Remember')  # Field name made lowercase.
    defaultbutton = models.SmallIntegerField(db_column='DefaultButton')  # Field name made lowercase.
    confirmed = models.BooleanField(db_column='Confirmed')  # Field name made lowercase.
    solution = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Message'


class Miangin(models.Model):
    miangin = models.DecimalField(db_column='Miangin', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    bagh = models.DecimalField(db_column='Bagh', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Miangin'


class Moshakhasat(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    companynamefield = models.CharField(db_column='CompanyNameField', max_length=250, blank=True, null=True)  # Field name made lowercase.
    oldeconomicnofield = models.CharField(db_column='OldEconomicNoField', max_length=50, blank=True, null=True)  # Field name made lowercase.
    neweconomicnofield = models.CharField(db_column='NewEconomicNoField', max_length=50, blank=True, null=True)  # Field name made lowercase.
    nationalcodefield = models.CharField(db_column='NationalCodeField', max_length=50, blank=True, null=True)  # Field name made lowercase.
    taxpayertypefield = models.CharField(db_column='TaxpayerTypeField', max_length=50, blank=True, null=True)  # Field name made lowercase.
    postalcodefield = models.CharField(db_column='PostalCodeField', max_length=50, blank=True, null=True)  # Field name made lowercase.
    statefield = models.CharField(db_column='StateField', max_length=50, blank=True, null=True)  # Field name made lowercase.
    cityfield = models.CharField(db_column='CityField', max_length=50, blank=True, null=True)  # Field name made lowercase.
    telcodefield = models.CharField(db_column='TelCodeField', max_length=10, blank=True, null=True)  # Field name made lowercase.
    telnofield = models.CharField(db_column='TelNoField', max_length=20, blank=True, null=True)  # Field name made lowercase.
    faxnofield = models.CharField(db_column='FaxNoField', max_length=20, blank=True, null=True)  # Field name made lowercase.
    registrationnofield = models.CharField(db_column='registrationNoField', max_length=50, blank=True, null=True)  # Field name made lowercase.
    hozehfield = models.CharField(db_column='HozehField', max_length=50, blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=500, blank=True, null=True)  # Field name made lowercase.
    countryfield = models.CharField(db_column='CountryField', max_length=50, blank=True, null=True)  # Field name made lowercase.
    shahrcode = models.IntegerField(db_column='ShahrCode', blank=True, null=True)  # Field name made lowercase.
    tabeiat = models.SmallIntegerField(db_column='Tabeiat', blank=True, null=True)  # Field name made lowercase.
    mobileno = models.CharField(db_column='MobileNO', max_length=11, blank=True, null=True)  # Field name made lowercase.
    edarekolcode = models.IntegerField(db_column='EdareKolCode', blank=True, null=True)  # Field name made lowercase.
    username = models.CharField(db_column='UserName', max_length=25, blank=True, null=True)  # Field name made lowercase.
    sabtenam = models.IntegerField(db_column='SabteNam', blank=True, null=True)  # Field name made lowercase.
    band = models.SmallIntegerField(db_column='Band', blank=True, null=True)  # Field name made lowercase.
    moadyname = models.CharField(db_column='MoadyName', max_length=250, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Moshakhasat'


class Note(models.Model):
    subject = models.CharField(db_column='SUBJECT', max_length=50, blank=True, null=True)  # Field name made lowercase.
    comment = models.CharField(db_column='COMMENT', max_length=500, blank=True, null=True)  # Field name made lowercase.
    row = models.AutoField(db_column='Row', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'NOTE'


class NewfeaturesList(models.Model):
    title = models.CharField(db_column='Title', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    softwareparts = models.CharField(db_column='SoftwareParts', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    softwarepartsread = models.CharField(db_column='SoftwarePartsRead', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    version = models.CharField(db_column='Version', max_length=10)  # Field name made lowercase.
    id = models.IntegerField(db_column='ID', blank=True, primary_key=True)  # Field name made lowercase.
    syncid = models.BigIntegerField(db_column='SyncID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'NewFeatures_List'


class News(models.Model):
    id = models.IntegerField(db_column='ID',primary_key=True)  # Field name made lowercase.
    title = models.TextField(blank=True, null=True)
    link = models.CharField(max_length=200, blank=True, null=True)
    kind = models.CharField(db_column='Kind', max_length=50, blank=True, null=True)  # Field name made lowercase.
    date = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'News'


class Notificationactions(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    notificationid = models.ForeignKey('Notifications', on_delete=models.DO_NOTHING, db_column='NotificationID')  # Field name made lowercase.
    priority = models.SmallIntegerField(db_column='Priority')  # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=100)  # Field name made lowercase.
    action = models.SmallIntegerField(db_column='Action')  # Field name made lowercase.
    parameter = models.CharField(db_column='Parameter', max_length=500, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'NotificationActions'


class Notificationusers(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    notificationid = models.ForeignKey('Notifications', on_delete=models.DO_NOTHING, db_column='NotificationID')  # Field name made lowercase.
    userid = models.IntegerField(db_column='UserID')  # Field name made lowercase.
    removed = models.BooleanField(db_column='Removed')  # Field name made lowercase.
    snoozed = models.BooleanField(db_column='Snoozed')  # Field name made lowercase.
    collapsed = models.BooleanField(db_column='Collapsed')  # Field name made lowercase.
    lastview = models.CharField(db_column='LastView', max_length=10, blank=True, null=True)  # Field name made lowercase.
    viewcount = models.IntegerField(db_column='ViewCount', blank=True, null=True)  # Field name made lowercase.
    action = models.SmallIntegerField(db_column='Action', blank=True, null=True)  # Field name made lowercase.
    softwareid = models.SmallIntegerField(db_column='SoftwareID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'NotificationUsers'


class Notifications(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    active = models.BooleanField(db_column='Active')  # Field name made lowercase.
    type = models.SmallIntegerField(db_column='Type')  # Field name made lowercase.
    usertype = models.SmallIntegerField(db_column='UserType')  # Field name made lowercase.
    icon = models.SmallIntegerField(db_column='Icon')  # Field name made lowercase.
    collapsable = models.BooleanField(db_column='Collapsable')  # Field name made lowercase.
    removable = models.BooleanField(db_column='Removable')  # Field name made lowercase.
    snoozable = models.BooleanField(db_column='Snoozable')  # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=100)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=1000)  # Field name made lowercase.
    portal_id = models.IntegerField(db_column='Portal_ID', blank=True, null=True)  # Field name made lowercase.
    expiredate = models.CharField(db_column='ExpireDate', max_length=10, blank=True, null=True)  # Field name made lowercase.
    expiretime = models.CharField(db_column='ExpireTime', max_length=5, blank=True, null=True)  # Field name made lowercase.
    expireshowcount = models.SmallIntegerField(db_column='ExpireShowCount', blank=True, null=True)  # Field name made lowercase.
    defaultbutton = models.SmallIntegerField(db_column='DefaultButton', blank=True, null=True)  # Field name made lowercase.
    cancelbutton = models.SmallIntegerField(db_column='CancelButton', blank=True, null=True)  # Field name made lowercase.
    offlinemode = models.BooleanField(db_column='OfflineMode', blank=True, null=True)  # Field name made lowercase.
    softwareid = models.SmallIntegerField(db_column='SoftwareID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Notifications'


class Obtain(models.Model):
    code = models.IntegerField(db_column='Code', primary_key=True)  # Field name made lowercase.
    grpassetcode = models.ForeignKey(Grpasset, on_delete=models.DO_NOTHING, db_column='GrpAssetCode')  # Field name made lowercase.
    entrancetype = models.CharField(db_column='EntranceType', max_length=50, blank=True, null=True)  # Field name made lowercase.
    actuary = models.CharField(db_column='Actuary', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sender = models.ForeignKey('Perinf', on_delete=models.DO_NOTHING, db_column='Sender')  # Field name made lowercase.
    reciever = models.CharField(db_column='Reciever', max_length=50, blank=True, null=True)  # Field name made lowercase.
    amount = models.DecimalField(db_column='Amount', max_digits=23, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    unitcost = models.DecimalField(db_column='UnitCost', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    depreciationstartdate = models.CharField(db_column='DepreciationStartDate', max_length=10)  # Field name made lowercase.
    orderid = models.CharField(db_column='OrderID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    receiptid = models.CharField(db_column='ReceiptID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    serialid = models.CharField(db_column='SerialID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    plateid = models.CharField(db_column='PlateID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    createyear = models.IntegerField(db_column='CreateYear', blank=True, null=True)  # Field name made lowercase.
    guaranty = models.BooleanField(db_column='Guaranty')  # Field name made lowercase.
    insurance = models.BooleanField(db_column='Insurance')  # Field name made lowercase.
    creator = models.CharField(db_column='Creator', max_length=50, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=50)  # Field name made lowercase.
    inductionplace = models.CharField(db_column='InductionPlace', max_length=50, blank=True, null=True)  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=50, blank=True, null=True)  # Field name made lowercase.
    model = models.CharField(db_column='Model', max_length=50, blank=True, null=True)  # Field name made lowercase.
    size = models.CharField(db_column='Size', max_length=50, blank=True, null=True)  # Field name made lowercase.
    usefulllife = models.IntegerField(db_column='UsefullLife', blank=True, null=True)  # Field name made lowercase.
    ruin = models.DecimalField(db_column='Ruin', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    junkcost = models.DecimalField(db_column='JunkCost', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    ruinunit = models.BooleanField(db_column='RuinUnit')  # Field name made lowercase.
    ruinmethod = models.IntegerField(db_column='RuinMethod', blank=True, null=True)  # Field name made lowercase.
    saveyear = models.SmallIntegerField(db_column='SaveYear', blank=True, null=True)  # Field name made lowercase.
    saveruin = models.DecimalField(db_column='SaveRuin', max_digits=23, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    comment = models.CharField(db_column='Comment', max_length=500, blank=True, null=True)  # Field name made lowercase.
    bgprd = models.BooleanField(db_column='bgPrd')  # Field name made lowercase.
    rateperecent = models.DecimalField(db_column='RatePerecent', max_digits=23, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    entrydate = models.CharField(db_column='EntryDate', max_length=10, blank=True, null=True)  # Field name made lowercase.
    vouchercode = models.IntegerField(db_column='VoucherCode', blank=True, null=True)  # Field name made lowercase.
    expcentercode = models.IntegerField(db_column='ExpCenterCode', blank=True, null=True)  # Field name made lowercase.
    createdtime = models.CharField(db_column='CreatedTime', max_length=5)  # Field name made lowercase.
    createddate = models.CharField(db_column='CreatedDate', max_length=10)  # Field name made lowercase.
    modifiedtime = models.CharField(db_column='ModifiedTime', max_length=5, blank=True, null=True)  # Field name made lowercase.
    modifieddate = models.CharField(db_column='ModifiedDate', max_length=10, blank=True, null=True)  # Field name made lowercase.
    usercreated = models.IntegerField(db_column='UserCreated')  # Field name made lowercase.
    usermodified = models.IntegerField(db_column='UserModified', blank=True, null=True)  # Field name made lowercase.
    owner = models.IntegerField(db_column='Owner')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Obtain'


class Onlineaccounttransfer(models.Model):
    mahaksyncid = models.BigIntegerField(db_column='MahakSyncID', blank=True, null=True)  # Field name made lowercase.
    transferid = models.BigIntegerField(db_column='TransferID', primary_key=True)  # Field name made lowercase.
    transfercode = models.CharField(db_column='TransferCode', max_length=100, blank=True, null=True)  # Field name made lowercase.
    transferdate = models.BigIntegerField(db_column='TransferDate', blank=True, null=True)  # Field name made lowercase.
    debittype = models.SmallIntegerField(db_column='DebitType', blank=True, null=True)  # Field name made lowercase.
    debitcode = models.IntegerField(db_column='DebitCode', blank=True, null=True)  # Field name made lowercase.
    credittype = models.SmallIntegerField(db_column='CreditType', blank=True, null=True)  # Field name made lowercase.
    creditcode = models.IntegerField(db_column='CreditCode', blank=True, null=True)  # Field name made lowercase.
    priceamount = models.DecimalField(db_column='PriceAmount', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    userid = models.IntegerField(db_column='UserID', blank=True, null=True)  # Field name made lowercase.
    comment = models.CharField(db_column='Comment', max_length=500, blank=True, null=True)  # Field name made lowercase.
    createby = models.CharField(db_column='CreateBy', max_length=100, blank=True, null=True)  # Field name made lowercase.
    createdate = models.BigIntegerField(db_column='CreateDate', blank=True, null=True)  # Field name made lowercase.
    modifyby = models.CharField(db_column='ModifyBy', max_length=100, blank=True, null=True)  # Field name made lowercase.
    modifydate = models.BigIntegerField(db_column='ModifyDate', blank=True, null=True)  # Field name made lowercase.
    isdelete = models.SmallIntegerField(db_column='IsDelete')  # Field name made lowercase.
    convertedto = models.BooleanField(db_column='ConvertedTo')  # Field name made lowercase.
    havalehesab_id = models.IntegerField(db_column='HavaleHesab_Id', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OnlineAccountTransfer'


class Onlinechecklist(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    mahakid = models.CharField(db_column='MahakID', max_length=100)  # Field name made lowercase.
    databaseid = models.CharField(db_column='DatabaseID', max_length=50)  # Field name made lowercase.
    masterid = models.IntegerField(db_column='MasterID')  # Field name made lowercase.
    userid = models.IntegerField(db_column='UserID', blank=True, null=True)  # Field name made lowercase.
    status = models.SmallIntegerField(db_column='Status', blank=True, null=True)  # Field name made lowercase.
    type = models.SmallIntegerField(db_column='Type', blank=True, null=True)  # Field name made lowercase.
    customerid = models.IntegerField(db_column='CustomerID', blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=500, blank=True, null=True)  # Field name made lowercase.
    createby = models.CharField(db_column='CreateBy', max_length=100, blank=True, null=True)  # Field name made lowercase.
    createdate = models.BigIntegerField(db_column='CreateDate', blank=True, null=True)  # Field name made lowercase.
    modifyby = models.CharField(db_column='ModifyBy', max_length=100, blank=True, null=True)  # Field name made lowercase.
    modifydate = models.BigIntegerField(db_column='ModifyDate', blank=True, null=True)  # Field name made lowercase.
    isdelete = models.SmallIntegerField(db_column='IsDelete')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OnlineCheckList'


class Onlinecheques(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    mahakid = models.CharField(db_column='MahakID', max_length=100)  # Field name made lowercase.
    databaseid = models.CharField(db_column='DatabaseID', max_length=50)  # Field name made lowercase.
    masterid = models.IntegerField(db_column='MasterID', blank=True, null=True)  # Field name made lowercase.
    receiptid = models.IntegerField(db_column='ReceiptID', blank=True, null=True)  # Field name made lowercase.
    number = models.CharField(db_column='Number', max_length=100, blank=True, null=True)  # Field name made lowercase.
    bank = models.CharField(db_column='Bank', max_length=100, blank=True, null=True)  # Field name made lowercase.
    branch = models.CharField(db_column='Branch', max_length=100, blank=True, null=True)  # Field name made lowercase.
    amount = models.DecimalField(db_column='Amount', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    date = models.BigIntegerField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
    type = models.SmallIntegerField(db_column='Type', blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=500, blank=True, null=True)  # Field name made lowercase.
    createby = models.CharField(db_column='CreateBy', max_length=100, blank=True, null=True)  # Field name made lowercase.
    createdate = models.BigIntegerField(db_column='CreateDate', blank=True, null=True)  # Field name made lowercase.
    modifyby = models.CharField(db_column='ModifyBy', max_length=100, blank=True, null=True)  # Field name made lowercase.
    modifydate = models.BigIntegerField(db_column='ModifyDate', blank=True, null=True)  # Field name made lowercase.
    isdelete = models.SmallIntegerField(db_column='IsDelete')  # Field name made lowercase.
    bankid = models.IntegerField(db_column='BankID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OnlineCheques'


class Onlinecustomers(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    masterid = models.IntegerField(db_column='MasterID', blank=True, null=True)  # Field name made lowercase.
    userid = models.CharField(db_column='UserID', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    latitude = models.DecimalField(db_column='Latitude', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    longitude = models.DecimalField(db_column='Longitude', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    isdelete = models.SmallIntegerField(db_column='IsDelete')  # Field name made lowercase.
    customercode = models.IntegerField(db_column='CustomerCode', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OnlineCustomers'


class Onlinedeliveryorders(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    mahakid = models.CharField(db_column='MahakID', max_length=100)  # Field name made lowercase.
    databaseid = models.CharField(db_column='DatabaseID', max_length=50)  # Field name made lowercase.
    masterid = models.IntegerField(db_column='MasterID', blank=True, null=True)  # Field name made lowercase.
    customerid = models.IntegerField(db_column='CustomerID', blank=True, null=True)  # Field name made lowercase.
    userid = models.IntegerField(db_column='UserID', blank=True, null=True)  # Field name made lowercase.
    deliverydate = models.BigIntegerField(db_column='DeliveryDate', blank=True, null=True)  # Field name made lowercase.
    discount = models.DecimalField(db_column='DisCount', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=500, blank=True, null=True)  # Field name made lowercase.
    settlementtype = models.SmallIntegerField(db_column='SettlementType', blank=True, null=True)  # Field name made lowercase.
    immediate = models.SmallIntegerField(db_column='Immediate', blank=True, null=True)  # Field name made lowercase.
    type = models.SmallIntegerField(db_column='Type', blank=True, null=True)  # Field name made lowercase.
    code = models.CharField(db_column='Code', max_length=100, blank=True, null=True)  # Field name made lowercase.
    createby = models.CharField(db_column='CreateBy', max_length=100, blank=True, null=True)  # Field name made lowercase.
    createdate = models.BigIntegerField(db_column='CreateDate', blank=True, null=True)  # Field name made lowercase.
    modifyby = models.CharField(db_column='ModifyBy', max_length=100, blank=True, null=True)  # Field name made lowercase.
    modifydate = models.BigIntegerField(db_column='ModifyDate', blank=True, null=True)  # Field name made lowercase.
    isdelete = models.SmallIntegerField(db_column='IsDelete', blank=True, null=True)  # Field name made lowercase.
    orderdate = models.BigIntegerField(db_column='OrderDate', blank=True, null=True)  # Field name made lowercase.
    convertedtopishfactor = models.BooleanField(db_column='ConvertedToPishFactor')  # Field name made lowercase.
    taxpercent = models.DecimalField(db_column='TaxPercent', max_digits=23, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    chargepercent = models.DecimalField(db_column='ChargePercent', max_digits=23, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    offpercent = models.DecimalField(db_column='Offpercent', max_digits=23, decimal_places=8, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OnlineDeliveryOrders'


class Onlinedetailsgoodtransfer(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    productid = models.IntegerField(db_column='ProductID', blank=True, null=True)  # Field name made lowercase.
    transferid = models.BigIntegerField(db_column='TransferID', blank=True, null=True)  # Field name made lowercase.
    count = models.DecimalField(db_column='Count', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    comment = models.CharField(db_column='Comment', max_length=500, blank=True, null=True)  # Field name made lowercase.
    createby = models.CharField(db_column='CreateBy', max_length=100, blank=True, null=True)  # Field name made lowercase.
    createdate = models.BigIntegerField(db_column='CreateDate', blank=True, null=True)  # Field name made lowercase.
    modifyby = models.CharField(db_column='ModifyBy', max_length=100, blank=True, null=True)  # Field name made lowercase.
    modifydate = models.BigIntegerField(db_column='ModifyDate', blank=True, null=True)  # Field name made lowercase.
    isdelete = models.SmallIntegerField(db_column='IsDelete')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OnlineDetailsGoodTransfer'


class Onlinedetailsinvoice(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    mahakid = models.CharField(db_column='MahakID', max_length=100)  # Field name made lowercase.
    databaseid = models.CharField(db_column='DatabaseID', max_length=50)  # Field name made lowercase.
    masterid = models.IntegerField(db_column='MasterID', blank=True, null=True)  # Field name made lowercase.
    productid = models.IntegerField(db_column='ProductID', blank=True, null=True)  # Field name made lowercase.
    orderid = models.IntegerField(db_column='OrderID', blank=True, null=True)  # Field name made lowercase.
    price = models.DecimalField(db_column='Price', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    count = models.DecimalField(db_column='Count', max_digits=23, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    gift = models.IntegerField(db_column='Gift', blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=500, blank=True, null=True)  # Field name made lowercase.
    createby = models.CharField(db_column='CreateBy', max_length=100, blank=True, null=True)  # Field name made lowercase.
    createdate = models.BigIntegerField(db_column='CreateDate', blank=True, null=True)  # Field name made lowercase.
    modifyby = models.CharField(db_column='ModifyBy', max_length=100, blank=True, null=True)  # Field name made lowercase.
    modifydate = models.BigIntegerField(db_column='ModifyDate', blank=True, null=True)  # Field name made lowercase.
    isdelete = models.SmallIntegerField(db_column='IsDelete')  # Field name made lowercase.
    taxpercent = models.DecimalField(db_column='TaxPercent', max_digits=23, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    chargepercent = models.DecimalField(db_column='ChargePercent', max_digits=23, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    offpercent = models.DecimalField(db_column='Offpercent', max_digits=23, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    gifttype = models.SmallIntegerField(db_column='GiftType', blank=True, null=True)  # Field name made lowercase.
    promotioncode = models.IntegerField(db_column='PromotionCode', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OnlineDetailsInvoice'


class Onlinefailureorders(models.Model):
    mahaksyncid = models.BigIntegerField(db_column='MahakSyncID')  # Field name made lowercase.
    masterid = models.BigIntegerField(db_column='MasterID', blank=True, null=True)  # Field name made lowercase.
    customerid = models.IntegerField(db_column='CustomerID', blank=True, null=True)  # Field name made lowercase.
    userid = models.IntegerField(db_column='UserID', blank=True, null=True)  # Field name made lowercase.
    faildate = models.BigIntegerField(db_column='FailDate', blank=True, null=True)  # Field name made lowercase.
    failcomment = models.CharField(db_column='FailComment', max_length=1500, blank=True, null=True)  # Field name made lowercase.
    code = models.CharField(db_column='Code', max_length=100, blank=True, null=True)  # Field name made lowercase.
    createby = models.CharField(db_column='CreateBy', max_length=100, blank=True, null=True)  # Field name made lowercase.
    createdate = models.BigIntegerField(db_column='CreateDate', blank=True, null=True)  # Field name made lowercase.
    modifyby = models.CharField(db_column='ModifyBy', max_length=100, blank=True, null=True)  # Field name made lowercase.
    modifydate = models.BigIntegerField(db_column='ModifyDate', blank=True, null=True)  # Field name made lowercase.
    isdelete = models.SmallIntegerField(db_column='IsDelete')  # Field name made lowercase.
    failorderid = models.IntegerField(db_column='FailOrderID', blank=True, null=True)  # Field name made lowercase.
    failreasonid = models.BigIntegerField(db_column='FailReasonID', blank=True, null=True)  # Field name made lowercase.
    jsondescription = models.TextField(db_column='JsonDescription', blank=True, null=True)  # Field name made lowercase.
    convertedto = models.BooleanField(db_column='ConvertedTo')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OnlineFailureOrders'


class Onlinegoodtransfer(models.Model):
    mahaksyncid = models.BigIntegerField(db_column='MahakSyncID', blank=True, null=True)  # Field name made lowercase.
    sendvisitorid = models.IntegerField(db_column='SendVisitorID', blank=True, null=True)  # Field name made lowercase.
    sendstoreid = models.IntegerField(db_column='SendStoreID', blank=True, null=True)  # Field name made lowercase.
    receivevisitorid = models.IntegerField(db_column='ReceiveVisitorID', blank=True, null=True)  # Field name made lowercase.
    receivestoreid = models.IntegerField(db_column='ReceiveStoreID', blank=True, null=True)  # Field name made lowercase.
    userid = models.IntegerField(db_column='UserID', blank=True, null=True)  # Field name made lowercase.
    transferdate = models.BigIntegerField(db_column='TransferDate', blank=True, null=True)  # Field name made lowercase.
    comment = models.CharField(db_column='Comment', max_length=500, blank=True, null=True)  # Field name made lowercase.
    transfercode = models.CharField(db_column='TransferCode', max_length=100, blank=True, null=True)  # Field name made lowercase.
    createby = models.CharField(db_column='CreateBy', max_length=100, blank=True, null=True)  # Field name made lowercase.
    createdate = models.BigIntegerField(db_column='CreateDate', blank=True, null=True)  # Field name made lowercase.
    modifyby = models.CharField(db_column='ModifyBy', max_length=100, blank=True, null=True)  # Field name made lowercase.
    modifydate = models.BigIntegerField(db_column='ModifyDate', blank=True, null=True)  # Field name made lowercase.
    isdelete = models.SmallIntegerField(db_column='IsDelete')  # Field name made lowercase.
    transferid = models.IntegerField(db_column='TransferID', primary_key=True)  # Field name made lowercase.
    convertedto = models.BooleanField(db_column='ConvertedTo')  # Field name made lowercase.
    havaleanbar_id = models.IntegerField(db_column='HavaleAnbar_Id', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OnlineGoodTransfer'


class Onlineinvoice(models.Model):
    mahakid = models.CharField(db_column='MahakID', max_length=100)  # Field name made lowercase.
    databaseid = models.CharField(db_column='DatabaseID', max_length=50)  # Field name made lowercase.
    masterid = models.BigIntegerField(db_column='MasterID', blank=True, null=True)  # Field name made lowercase.
    customerid = models.IntegerField(db_column='CustomerID', blank=True, null=True)  # Field name made lowercase.
    userid = models.IntegerField(db_column='UserID', blank=True, null=True)  # Field name made lowercase.
    orderdate = models.BigIntegerField(db_column='OrderDate', blank=True, null=True)  # Field name made lowercase.
    deliverydate = models.BigIntegerField(db_column='DeliveryDate', blank=True, null=True)  # Field name made lowercase.
    discount = models.DecimalField(db_column='DisCount', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=500, blank=True, null=True)  # Field name made lowercase.
    settlementtype = models.SmallIntegerField(db_column='SettlementType', blank=True, null=True)  # Field name made lowercase.
    immediate = models.SmallIntegerField(db_column='Immediate', blank=True, null=True)  # Field name made lowercase.
    type = models.SmallIntegerField(db_column='Type', blank=True, null=True)  # Field name made lowercase.
    code = models.CharField(db_column='Code', max_length=100, blank=True, null=True)  # Field name made lowercase.
    createby = models.CharField(db_column='CreateBy', max_length=100, blank=True, null=True)  # Field name made lowercase.
    createdate = models.BigIntegerField(db_column='CreateDate', blank=True, null=True)  # Field name made lowercase.
    modifyby = models.CharField(db_column='ModifyBy', max_length=100, blank=True, null=True)  # Field name made lowercase.
    modifydate = models.BigIntegerField(db_column='ModifyDate', blank=True, null=True)  # Field name made lowercase.
    isdelete = models.SmallIntegerField(db_column='IsDelete')  # Field name made lowercase.
    ordertype = models.SmallIntegerField(db_column='OrderType', blank=True, null=True)  # Field name made lowercase.
    id = models.IntegerField(blank=True, primary_key=True)
    jsondescription = models.TextField(db_column='JsonDescription', blank=True, null=True)  # Field name made lowercase.
    convertedtopishfactor = models.BooleanField(db_column='ConvertedToPishFactor')  # Field name made lowercase.
    factfo_id = models.IntegerField(db_column='FactFo_Id', blank=True, null=True)  # Field name made lowercase.
    gifttype = models.SmallIntegerField(db_column='GiftType', blank=True, null=True)  # Field name made lowercase.
    promotioncode = models.IntegerField(db_column='PromotionCode', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OnlineInvoice'


class Onlineorder(models.Model):
    mahakid = models.CharField(db_column='MahakID', max_length=100)  # Field name made lowercase.
    databaseid = models.CharField(db_column='DatabaseID', max_length=50)  # Field name made lowercase.
    masterid = models.BigIntegerField(db_column='MasterID', blank=True, null=True)  # Field name made lowercase.
    customerid = models.IntegerField(db_column='CustomerID', blank=True, null=True)  # Field name made lowercase.
    userid = models.IntegerField(db_column='UserID', blank=True, null=True)  # Field name made lowercase.
    orderdate = models.BigIntegerField(db_column='OrderDate', blank=True, null=True)  # Field name made lowercase.
    deliverydate = models.BigIntegerField(db_column='DeliveryDate', blank=True, null=True)  # Field name made lowercase.
    discount = models.DecimalField(db_column='DisCount', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=500, blank=True, null=True)  # Field name made lowercase.
    settlementtype = models.SmallIntegerField(db_column='SettlementType', blank=True, null=True)  # Field name made lowercase.
    immediate = models.SmallIntegerField(db_column='Immediate', blank=True, null=True)  # Field name made lowercase.
    type = models.SmallIntegerField(db_column='Type', blank=True, null=True)  # Field name made lowercase.
    code = models.CharField(db_column='Code', max_length=100, blank=True, null=True)  # Field name made lowercase.
    createby = models.CharField(db_column='CreateBy', max_length=100, blank=True, null=True)  # Field name made lowercase.
    createdate = models.BigIntegerField(db_column='CreateDate', blank=True, null=True)  # Field name made lowercase.
    modifyby = models.CharField(db_column='ModifyBy', max_length=100, blank=True, null=True)  # Field name made lowercase.
    modifydate = models.BigIntegerField(db_column='ModifyDate', blank=True, null=True)  # Field name made lowercase.
    isdelete = models.SmallIntegerField(db_column='IsDelete')  # Field name made lowercase.
    ordertype = models.SmallIntegerField(db_column='OrderType', blank=True, null=True)  # Field name made lowercase.
    id = models.IntegerField(primary_key=True)
    jsondescription = models.TextField(db_column='JsonDescription', blank=True, null=True)  # Field name made lowercase.
    convertedtopishfactor = models.BooleanField(db_column='ConvertedToPishFactor')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OnlineOrder'


class Onlinepicture(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    mahakid = models.CharField(db_column='MahakID', max_length=100)  # Field name made lowercase.
    databaseid = models.CharField(db_column='DatabaseID', max_length=50)  # Field name made lowercase.
    picturecode = models.IntegerField(db_column='PictureCode')  # Field name made lowercase.
    lastuploadedhash = models.CharField(db_column='LastUploadedHash', max_length=50, blank=True, null=True)  # Field name made lowercase.
    successcount = models.IntegerField(db_column='SuccessCount')  # Field name made lowercase.
    failedcount = models.IntegerField(db_column='FailedCount')  # Field name made lowercase.
    lastsuccesstime = models.DateTimeField(db_column='LastSuccessTime', blank=True, null=True)  # Field name made lowercase.
    lastfailedtime = models.DateTimeField(db_column='LastFailedTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OnlinePicture'


class Onlineproduct(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    mahakid = models.CharField(db_column='MahakID', max_length=100, blank=True, null=True)  # Field name made lowercase.
    databaseid = models.CharField(db_column='DatabaseID', max_length=100, blank=True, null=True)  # Field name made lowercase.
    masterid = models.IntegerField(db_column='MasterID', blank=True, null=True)  # Field name made lowercase.
    categoryid = models.IntegerField(db_column='CategoryID', blank=True, null=True)  # Field name made lowercase.
    productcode = models.IntegerField(db_column='ProductCode', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=150, blank=True, null=True)  # Field name made lowercase.
    asset = models.IntegerField(db_column='Asset', blank=True, null=True)  # Field name made lowercase.
    asset2 = models.IntegerField(db_column='Asset2', blank=True, null=True)  # Field name made lowercase.
    price = models.DecimalField(db_column='Price', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    tags = models.CharField(db_column='Tags', max_length=500, blank=True, null=True)  # Field name made lowercase.
    customerprice = models.DecimalField(db_column='CustomerPrice', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    inbox = models.IntegerField(db_column='InBox', blank=True, null=True)  # Field name made lowercase.
    code = models.CharField(db_column='Code', max_length=100, blank=True, null=True)  # Field name made lowercase.
    image = models.CharField(db_column='Image', max_length=250, blank=True, null=True)  # Field name made lowercase.
    min = models.IntegerField(db_column='Min', blank=True, null=True)  # Field name made lowercase.
    createby = models.CharField(db_column='CreateBy', max_length=100, blank=True, null=True)  # Field name made lowercase.
    createdate = models.BigIntegerField(db_column='CreateDate', blank=True, null=True)  # Field name made lowercase.
    modifyby = models.CharField(db_column='ModifyBy', max_length=100, blank=True, null=True)  # Field name made lowercase.
    modifydate = models.BigIntegerField(db_column='ModifyDate', blank=True, null=True)  # Field name made lowercase.
    isdelete = models.SmallIntegerField(db_column='IsDelete', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OnlineProduct'


class Onlineproductinusers(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    mahakid = models.CharField(db_column='MahakID', max_length=100)  # Field name made lowercase.
    databaseid = models.CharField(db_column='DatabaseID', max_length=50)  # Field name made lowercase.
    masterid = models.IntegerField(db_column='MasterID', blank=True, null=True)  # Field name made lowercase.
    productid = models.IntegerField(db_column='ProductID', blank=True, null=True)  # Field name made lowercase.
    userid = models.IntegerField(db_column='UserID', blank=True, null=True)  # Field name made lowercase.
    asset = models.DecimalField(db_column='Asset', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    asset1 = models.DecimalField(db_column='Asset1', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    price = models.DecimalField(db_column='Price', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    createby = models.CharField(db_column='CreateBy', max_length=100, blank=True, null=True)  # Field name made lowercase.
    createdate = models.BigIntegerField(db_column='CreateDate', blank=True, null=True)  # Field name made lowercase.
    modifyby = models.CharField(db_column='ModifyBy', max_length=100, blank=True, null=True)  # Field name made lowercase.
    modifydate = models.BigIntegerField(db_column='ModifyDate', blank=True, null=True)  # Field name made lowercase.
    isdelete = models.SmallIntegerField(db_column='IsDelete', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OnlineProductInUsers'


class Onlineproductsinorder(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    mahakid = models.CharField(db_column='MahakID', max_length=100)  # Field name made lowercase.
    databaseid = models.CharField(db_column='DatabaseID', max_length=50)  # Field name made lowercase.
    masterid = models.IntegerField(db_column='MasterID', blank=True, null=True)  # Field name made lowercase.
    productid = models.IntegerField(db_column='ProductID', blank=True, null=True)  # Field name made lowercase.
    orderid = models.IntegerField(db_column='OrderID', blank=True, null=True)  # Field name made lowercase.
    price = models.DecimalField(db_column='Price', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    count = models.DecimalField(db_column='Count', max_digits=23, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    gift = models.IntegerField(db_column='Gift', blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=500, blank=True, null=True)  # Field name made lowercase.
    createby = models.CharField(db_column='CreateBy', max_length=100, blank=True, null=True)  # Field name made lowercase.
    createdate = models.BigIntegerField(db_column='CreateDate', blank=True, null=True)  # Field name made lowercase.
    modifyby = models.CharField(db_column='ModifyBy', max_length=100, blank=True, null=True)  # Field name made lowercase.
    modifydate = models.BigIntegerField(db_column='ModifyDate', blank=True, null=True)  # Field name made lowercase.
    isdelete = models.SmallIntegerField(db_column='IsDelete')  # Field name made lowercase.
    taxpercent = models.DecimalField(db_column='TaxPercent', max_digits=23, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    chargepercent = models.DecimalField(db_column='ChargePercent', max_digits=23, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    offpercent = models.DecimalField(db_column='Offpercent', max_digits=23, decimal_places=8, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OnlineProductsInOrder'


class Onlinereceipts(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    mahakid = models.CharField(db_column='MahakID', max_length=100)  # Field name made lowercase.
    databaseid = models.CharField(db_column='DatabaseID', max_length=50)  # Field name made lowercase.
    masterid = models.BigIntegerField(db_column='MasterID', blank=True, null=True)  # Field name made lowercase.
    customerid = models.IntegerField(db_column='CustomerID', blank=True, null=True)  # Field name made lowercase.
    cashamount = models.DecimalField(db_column='CashAmount', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=500, blank=True, null=True)  # Field name made lowercase.
    userid = models.IntegerField(db_column='UserID', blank=True, null=True)  # Field name made lowercase.
    date = models.BigIntegerField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
    createby = models.CharField(db_column='CreateBy', max_length=100, blank=True, null=True)  # Field name made lowercase.
    createdate = models.BigIntegerField(db_column='CreateDate', blank=True, null=True)  # Field name made lowercase.
    modifyby = models.CharField(db_column='ModifyBy', max_length=100, blank=True, null=True)  # Field name made lowercase.
    modifydate = models.BigIntegerField(db_column='ModifyDate', blank=True, null=True)  # Field name made lowercase.
    isdelete = models.SmallIntegerField(db_column='IsDelete')  # Field name made lowercase.
    convertedtopishfactor = models.BooleanField(db_column='ConvertedToPishfactor')  # Field name made lowercase.
    getrecive_id = models.IntegerField(db_column='GetRecive_Id', blank=True, null=True)  # Field name made lowercase.
    trackingcode = models.CharField(db_column='TrackingCode', max_length=20, blank=True, null=True)  # Field name made lowercase.
    cashcode = models.IntegerField(db_column='CashCode', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OnlineReceipts'


class Onlinereturninvoice(models.Model):
    mahaksyncid = models.BigIntegerField(db_column='MahakSyncID')  # Field name made lowercase.
    masterid = models.BigIntegerField(db_column='MasterID', blank=True, null=True)  # Field name made lowercase.
    customerid = models.IntegerField(db_column='CustomerID', blank=True, null=True)  # Field name made lowercase.
    userid = models.IntegerField(db_column='UserID', blank=True, null=True)  # Field name made lowercase.
    returndate = models.BigIntegerField(db_column='ReturnDate', blank=True, null=True)  # Field name made lowercase.
    discount = models.DecimalField(db_column='Discount', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    compensationprice = models.DecimalField(db_column='CompensationPrice', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=1500, blank=True, null=True)  # Field name made lowercase.
    code = models.CharField(db_column='Code', max_length=100, blank=True, null=True)  # Field name made lowercase.
    createby = models.CharField(db_column='CreateBy', max_length=100, blank=True, null=True)  # Field name made lowercase.
    createdate = models.BigIntegerField(db_column='CreateDate', blank=True, null=True)  # Field name made lowercase.
    modifyby = models.CharField(db_column='ModifyBy', max_length=100, blank=True, null=True)  # Field name made lowercase.
    modifydate = models.BigIntegerField(db_column='ModifyDate', blank=True, null=True)  # Field name made lowercase.
    isdelete = models.SmallIntegerField(db_column='IsDelete')  # Field name made lowercase.
    rinvoiceid = models.IntegerField(db_column='RInvoiceID', blank=True, null=True)  # Field name made lowercase.
    rreasonid = models.BigIntegerField(db_column='RReasonID', blank=True, null=True)  # Field name made lowercase.
    jsondescription = models.TextField(db_column='JsonDescription', blank=True, null=True)  # Field name made lowercase.
    convertedto = models.BooleanField(db_column='ConvertedTo')  # Field name made lowercase.
    backforosh_id = models.IntegerField(db_column='BackForosh_Id', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OnlineReturnInvoice'


class Onlinereturninvoicedetails(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    returninvoiceid = models.BigIntegerField(db_column='ReturnInvoiceID', blank=True, null=True)  # Field name made lowercase.
    productid = models.IntegerField(db_column='ProductID', blank=True, null=True)  # Field name made lowercase.
    price = models.DecimalField(db_column='Price', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    count = models.DecimalField(db_column='Count', max_digits=23, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=500, blank=True, null=True)  # Field name made lowercase.
    createby = models.CharField(db_column='CreateBy', max_length=100, blank=True, null=True)  # Field name made lowercase.
    createdate = models.BigIntegerField(db_column='CreateDate', blank=True, null=True)  # Field name made lowercase.
    modifyby = models.CharField(db_column='ModifyBy', max_length=100, blank=True, null=True)  # Field name made lowercase.
    modifydate = models.BigIntegerField(db_column='ModifyDate', blank=True, null=True)  # Field name made lowercase.
    isdelete = models.SmallIntegerField(db_column='IsDelete')  # Field name made lowercase.
    saleinvoicecode = models.IntegerField(db_column='SaleInvoiceCode', blank=True, null=True)  # Field name made lowercase.
    saleinvoicedetailrow = models.IntegerField(db_column='SaleInvoiceDetailRow', blank=True, null=True)  # Field name made lowercase.
    taxpercent = models.DecimalField(db_column='TaxPercent', max_digits=23, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    chargepercent = models.DecimalField(db_column='ChargePercent', max_digits=23, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    offpercent = models.DecimalField(db_column='Offpercent', max_digits=23, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    convertedto = models.BooleanField(db_column='ConvertedTo')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OnlineReturnInvoiceDetails'


class Onlinetransaction(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    mahakid = models.CharField(db_column='MahakID', max_length=100)  # Field name made lowercase.
    databaseid = models.CharField(db_column='DatabaseID', max_length=50)  # Field name made lowercase.
    masterid = models.IntegerField(db_column='MasterID', blank=True, null=True)  # Field name made lowercase.
    customerid = models.IntegerField(db_column='CustomerID', blank=True, null=True)  # Field name made lowercase.
    transactionid = models.IntegerField(db_column='TransactionID', blank=True, null=True)  # Field name made lowercase.
    type = models.SmallIntegerField(db_column='Type', blank=True, null=True)  # Field name made lowercase.
    debitamount = models.DecimalField(db_column='DebitAmount', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    creditamount = models.DecimalField(db_column='CreditAmount', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    remainedamount = models.DecimalField(db_column='RemainedAmount', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=50, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=500, blank=True, null=True)  # Field name made lowercase.
    createby = models.CharField(db_column='CreateBy', max_length=100, blank=True, null=True)  # Field name made lowercase.
    createdate = models.BigIntegerField(db_column='CreateDate', blank=True, null=True)  # Field name made lowercase.
    modifyby = models.CharField(db_column='ModifyBy', max_length=100, blank=True, null=True)  # Field name made lowercase.
    modifydate = models.BigIntegerField(db_column='ModifyDate', blank=True, null=True)  # Field name made lowercase.
    isdelete = models.SmallIntegerField(db_column='IsDelete')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OnlineTransaction'


class Onlineuser(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    mahakid = models.CharField(db_column='MahakID', max_length=100, blank=True, null=True)  # Field name made lowercase.
    databaseid = models.CharField(db_column='DatabaseID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    masterid = models.IntegerField(db_column='MasterID', blank=True, null=True)  # Field name made lowercase.
    packageserial = models.CharField(db_column='PackageSerial', max_length=20, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=150, blank=True, null=True)  # Field name made lowercase.
    username = models.CharField(db_column='UserName', max_length=150)  # Field name made lowercase.
    acccode = models.IntegerField(db_column='AccCode')  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=150, blank=True, null=True)  # Field name made lowercase.
    type = models.SmallIntegerField(db_column='Type', blank=True, null=True)  # Field name made lowercase.
    deviceid = models.CharField(db_column='DeviceID', max_length=500, blank=True, null=True)  # Field name made lowercase.
    tell = models.CharField(db_column='Tell', max_length=20, blank=True, null=True)  # Field name made lowercase.
    gcmid = models.CharField(db_column='GCMID', max_length=250, blank=True, null=True)  # Field name made lowercase.
    syncid = models.BigIntegerField(db_column='SyncID', blank=True, null=True)  # Field name made lowercase.
    createby = models.CharField(db_column='CreateBy', max_length=100, blank=True, null=True)  # Field name made lowercase.
    createdate = models.BigIntegerField(db_column='CreateDate', blank=True, null=True)  # Field name made lowercase.
    modifyby = models.CharField(db_column='ModifyBy', max_length=100, blank=True, null=True)  # Field name made lowercase.
    modifydate = models.BigIntegerField(db_column='ModifyDate', blank=True, null=True)  # Field name made lowercase.
    isdelete = models.SmallIntegerField(db_column='IsDelete')  # Field name made lowercase.
    storecode = models.IntegerField(db_column='StoreCode', blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=200, blank=True, null=True)  # Field name made lowercase.
    isactive = models.BooleanField(db_column='IsActive')  # Field name made lowercase.
    bankcode = models.IntegerField(db_column='BankCode', blank=True, null=True)  # Field name made lowercase.
    cashcode = models.IntegerField(db_column='CashCode', blank=True, null=True)  # Field name made lowercase.
    priceaccess = models.BooleanField(db_column='PriceAccess', blank=True, null=True)  # Field name made lowercase.
    costlevelaccess = models.BooleanField(db_column='CostLevelAccess', blank=True, null=True)  # Field name made lowercase.
    sell_defaultcostlevel = models.IntegerField(db_column='Sell_DefaultCostLevel', blank=True, null=True)  # Field name made lowercase.
    selectedcostlevels = models.CharField(db_column='SelectedCostLevels', max_length=50, blank=True, null=True)  # Field name made lowercase.
    totalcredit = models.BigIntegerField(db_column='TotalCredit', blank=True, null=True)  # Field name made lowercase.
    chequecredit = models.BigIntegerField(db_column='ChequeCredit', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OnlineUser'


class OpeningvoucherLastmanualdetails(models.Model):
    code = models.IntegerField()
    radif = models.IntegerField()
    kol = models.SmallIntegerField(blank=True, null=True)
    moin = models.SmallIntegerField(blank=True, null=True)
    tafzili = models.IntegerField(blank=True, null=True)
    sharh = models.CharField(max_length=500, blank=True, null=True)
    status = models.SmallIntegerField(blank=True, null=True)
    bed = models.DecimalField(max_digits=23, decimal_places=9, blank=True, null=True)
    bes = models.DecimalField(max_digits=23, decimal_places=9, blank=True, null=True)
    sanad_code = models.CharField(db_column='Sanad_Code', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sanad_type = models.IntegerField(db_column='Sanad_Type', blank=True, null=True)  # Field name made lowercase.
    meghdar = models.DecimalField(db_column='Meghdar', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    com_index = models.IntegerField(db_column='Com_Index')  # Field name made lowercase.
    zamaem = models.IntegerField(db_column='Zamaem', blank=True, null=True)  # Field name made lowercase.
    store = models.SmallIntegerField(db_column='Store', blank=True, null=True)  # Field name made lowercase.
    tafsili2 = models.IntegerField(db_column='Tafsili2', blank=True, null=True)  # Field name made lowercase.
    voucherdate = models.CharField(db_column='VoucherDate', max_length=10, blank=True, null=True)  # Field name made lowercase.
    operationdate = models.CharField(db_column='OperationDate', max_length=10, blank=True, null=True)  # Field name made lowercase.
    syscomment = models.CharField(db_column='SysComment', max_length=1100, blank=True, null=True)  # Field name made lowercase.
    currcode = models.IntegerField(db_column='CurrCode', blank=True, null=True)  # Field name made lowercase.
    curramount = models.DecimalField(db_column='CurrAmount', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    currrate = models.DecimalField(db_column='CurrRate', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    usercode = models.IntegerField(db_column='UserCode', blank=True, null=True)  # Field name made lowercase.
    global_id = models.IntegerField(db_column='Global_ID', blank=True, null=True)  # Field name made lowercase.
    createdtime = models.CharField(db_column='CreatedTime', max_length=5, blank=True, null=True)  # Field name made lowercase.
    createddate = models.CharField(db_column='CreatedDate', max_length=10, blank=True, null=True)  # Field name made lowercase.
    modifiedtime = models.CharField(db_column='ModifiedTime', max_length=5, blank=True, null=True)  # Field name made lowercase.
    modifieddate = models.CharField(db_column='ModifiedDate', max_length=10, blank=True, null=True)  # Field name made lowercase.
    usercreated = models.CharField(db_column='UserCreated', max_length=50, blank=True, null=True)  # Field name made lowercase.
    usermodified = models.CharField(db_column='UserModified', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OpeningVoucher_LastManualDetails'


class Oppositeaccs(models.Model):
    rowid =  models.AutoField(db_column='RowID', primary_key=True)  # Field name made lowercase.
    kol = models.IntegerField(db_column='Kol', blank=True, null=True)  # Field name made lowercase.
    moin = models.IntegerField(db_column='Moin', blank=True, null=True)  # Field name made lowercase.
    tafsili = models.IntegerField(db_column='Tafsili', blank=True, null=True)  # Field name made lowercase.
    tafsili2 = models.IntegerField(db_column='Tafsili2', blank=True, null=True)  # Field name made lowercase.
    descr = models.CharField(db_column='Descr', max_length=300, blank=True, null=True)  # Field name made lowercase.
    accname = models.CharField(db_column='AccName', max_length=300, blank=True, null=True)  # Field name made lowercase.
    debit = models.DecimalField(db_column='Debit', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    credit = models.DecimalField(db_column='Credit', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    acctype = models.SmallIntegerField(db_column='AccType', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OppositeAccs'


class Options(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    voicepath = models.CharField(db_column='VoicePath', max_length=255, blank=True, null=True)  # Field name made lowercase.
    codenum = models.CharField(db_column='CodeNum', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sounddevice = models.CharField(db_column='SoundDevice', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Options'


class Order(models.Model):
    code = models.IntegerField(db_column='Code', primary_key=True)  # Field name made lowercase.
    percode = models.ForeignKey('Perinf', on_delete=models.DO_NOTHING, db_column='PerCode')  # Field name made lowercase.
    date = models.CharField(db_column='Date', max_length=10)  # Field name made lowercase.
    usercreated = models.ForeignKey('Users', on_delete=models.DO_NOTHING, db_column='UserCreated')  # Field name made lowercase.
    comment = models.CharField(db_column='Comment', max_length=500, blank=True, null=True)  # Field name made lowercase.
    createdtime = models.CharField(db_column='CreatedTime', max_length=5)  # Field name made lowercase.
    createddate = models.CharField(db_column='CreatedDate', max_length=10)  # Field name made lowercase.
    modifiedtime = models.CharField(db_column='ModifiedTime', max_length=5, blank=True, null=True)  # Field name made lowercase.
    modifieddate = models.CharField(db_column='ModifiedDate', max_length=10, blank=True, null=True)  # Field name made lowercase.
    usermodified = models.IntegerField(db_column='UserModified', blank=True, null=True)  # Field name made lowercase.
    owner = models.IntegerField(db_column='Owner')  # Field name made lowercase.
    type = models.SmallIntegerField(db_column='Type')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Order'


class Orderdetail(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    ordercode = models.ForeignKey(Order, on_delete=models.DO_NOTHING, db_column='OrderCode')  # Field name made lowercase.
    storecode = models.ForeignKey('Stores', on_delete=models.DO_NOTHING, db_column='Storecode', blank=True, null=True)  # Field name made lowercase.
    goodcode = models.ForeignKey(Goodinf, on_delete=models.DO_NOTHING, db_column='Goodcode')  # Field name made lowercase.
    comment = models.CharField(db_column='Comment', max_length=500, blank=True, null=True)  # Field name made lowercase.
    amount = models.DecimalField(db_column='Amount', max_digits=23, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    naghdi = models.DecimalField(max_digits=23, decimal_places=9, blank=True, null=True)
    tool = models.DecimalField(max_digits=23, decimal_places=8, blank=True, null=True)
    arz = models.DecimalField(max_digits=23, decimal_places=8, blank=True, null=True)
    tedad = models.IntegerField(blank=True, null=True)
    amount2 = models.DecimalField(db_column='Amount2', max_digits=23, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    ghotr = models.DecimalField(max_digits=23, decimal_places=8, blank=True, null=True)
    reval = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'OrderDetail'


class Partpermission(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    partcode = models.ForeignKey('Softwarepart', on_delete=models.DO_NOTHING, db_column='PartCode')  # Field name made lowercase.
    permissionid = models.ForeignKey('Permission', on_delete=models.DO_NOTHING, db_column='PermissionID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PartPermission'
        unique_together = (('partcode', 'permissionid'),)


class PayrecieveVisitor(models.Model):
    id = id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    fact_code = models.IntegerField(blank=True, null=True)
    per_code = models.IntegerField(db_column='Per_code', blank=True, null=True)  # Field name made lowercase.
    tmp = models.BooleanField(blank=True, null=True)
    fact_tmp = models.BooleanField(db_column='Fact_TMP', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PayRecieve_Visitor'


class Payrollinfo(models.Model):
    code = models.IntegerField(db_column='Code')  # Field name made lowercase.
    value = models.CharField(db_column='Value', max_length=300)  # Field name made lowercase.
    comment = models.CharField(db_column='Comment', max_length=500, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PayrollInfo'


class Payrollinfodetail(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    type = models.BooleanField(db_column='Type')  # Field name made lowercase.
    code = models.IntegerField(db_column='Code')  # Field name made lowercase.
    usercode = models.IntegerField(db_column='UserCode')  # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PayrollInfoDetail'


class Pergrp(models.Model):
    code = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    status = models.SmallIntegerField(db_column='Status', blank=True, null=True)  # Field name made lowercase.
    sell_defaultcostlevel = models.IntegerField(db_column='Sell_DefaultCostLevel', blank=True, null=True)  # Field name made lowercase.
    buy_defaultcostlevel = models.IntegerField(db_column='Buy_DefaultCostLevel', blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return self.name if self.name else f"گروه شخص کد {self.code}"

    class Meta:
        managed = False
        db_table = 'PerGrp'


class Perinf(models.Model):
    code = models.IntegerField(primary_key=True)
    name = models.CharField(db_column='Name', max_length=50, blank=True, null=True)  # Field name made lowercase.
    lname = models.CharField(db_column='LName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    grpcode = models.ForeignKey(Pergrp, on_delete=models.DO_NOTHING, db_column='GrpCode', blank=True, null=True)  # Field name made lowercase.
    identifier = models.CharField(db_column='Identifier', max_length=50, blank=True, null=True)  # Field name made lowercase.
    comname = models.CharField(db_column='ComName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    tel1 = models.CharField(db_column='Tel1', max_length=50, blank=True, null=True)  # Field name made lowercase.
    tel2 = models.CharField(db_column='Tel2', max_length=50, blank=True, null=True)  # Field name made lowercase.
    fax = models.CharField(db_column='Fax', max_length=50, blank=True, null=True)  # Field name made lowercase.
    mobile = models.CharField(db_column='Mobile', max_length=50, blank=True, null=True)  # Field name made lowercase.
    addr1 = models.CharField(db_column='Addr1', max_length=300, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=50, blank=True, null=True)  # Field name made lowercase.
    comment = models.CharField(db_column='Comment', max_length=500, blank=True, null=True)  # Field name made lowercase.
    credit = models.DecimalField(db_column='Credit', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    sitbgprd = models.SmallIntegerField(db_column='SitBgPrd')  # Field name made lowercase.
    remainbgprd = models.DecimalField(db_column='RemainBgPrd', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    sitprd = models.SmallIntegerField(db_column='SitPrd', blank=True, null=True)  # Field name made lowercase.
    remainprd = models.DecimalField(db_column='RemainPrd', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    status = models.SmallIntegerField(db_column='Status', blank=True, null=True)  # Field name made lowercase.
    mandeh_check = models.DecimalField(max_digits=23, decimal_places=9, blank=True, null=True)
    fullname = models.CharField(unique=True, max_length=171, blank=True, null=True)
    percent = models.DecimalField(db_column='Percent', max_digits=23, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    vouchercode = models.IntegerField(db_column='VoucherCode', blank=True, null=True)  # Field name made lowercase.
    lastprintdate = models.CharField(db_column='LastPrintDate', max_length=10, blank=True, null=True)  # Field name made lowercase.
    economicno = models.CharField(db_column='EconomicNo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    regno = models.CharField(db_column='RegNo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    postcode_high = models.CharField(db_column='PostCode_High', max_length=5, blank=True, null=True)  # Field name made lowercase.
    postcode_low = models.CharField(db_column='PostCode_Low', max_length=5, blank=True, null=True)  # Field name made lowercase.
    username = models.CharField(db_column='UserName', unique=True, max_length=50, blank=True, null=True)  # Field name made lowercase.
    password = models.CharField(db_column='PASSWORD', max_length=30, blank=True, null=True)  # Field name made lowercase.
    prifix = models.CharField(db_column='Prifix', max_length=20, blank=True, null=True)  # Field name made lowercase.
    brthday = models.CharField(db_column='BrthDay', max_length=10, blank=True, null=True)  # Field name made lowercase.
    islegal = models.SmallIntegerField(db_column='IsLegal', blank=True, null=True)  # Field name made lowercase.
    off_percent = models.DecimalField(db_column='Off_Percent', max_digits=23, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    percent_driver = models.DecimalField(db_column='Percent_Driver', max_digits=23, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    currcode = models.IntegerField(db_column='CurrCode', blank=True, null=True)  # Field name made lowercase.
    currrate = models.DecimalField(db_column='CurrRate', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    currdefault = models.IntegerField(db_column='CurrDefault', blank=True, null=True)  # Field name made lowercase.
    tags = models.CharField(max_length=100, blank=True, null=True)
    sh_meli = models.CharField(db_column='Sh_meli', max_length=15, blank=True, null=True)  # Field name made lowercase.
    sell_defaultcostlevel = models.IntegerField(db_column='Sell_DefaultCostLevel', blank=True, null=True)  # Field name made lowercase.
    buy_defaultcostlevel = models.IntegerField(db_column='Buy_DefaultCostLevel', blank=True, null=True)  # Field name made lowercase.
    sh_h = models.CharField(db_column='Sh_h', max_length=50, blank=True, null=True)  # Field name made lowercase.
    citycode = models.IntegerField(db_column='CityCode', blank=True, null=True)  # Field name made lowercase.
    longitude = models.DecimalField(max_digits=18, decimal_places=15, blank=True, null=True)
    latitude = models.DecimalField(max_digits=18, decimal_places=15, blank=True, null=True)
    visitorcode = models.IntegerField(db_column='VisitorCode', blank=True, null=True)  # Field name made lowercase.
    createdtime = models.CharField(db_column='CreatedTime', max_length=5, blank=True, null=True)  # Field name made lowercase.
    createddate = models.CharField(db_column='CreatedDate', max_length=10, blank=True, null=True)  # Field name made lowercase.
    modifiedtime = models.CharField(db_column='ModifiedTime', max_length=5, blank=True, null=True)  # Field name made lowercase.
    modifieddate = models.CharField(db_column='ModifiedDate', max_length=10, blank=True, null=True)  # Field name made lowercase.
    usercreated = models.CharField(db_column='UserCreated', max_length=50, blank=True, null=True)  # Field name made lowercase.
    usermodified = models.CharField(db_column='UserModified', max_length=50, blank=True, null=True)  # Field name made lowercase.
    subscriberid = models.IntegerField(db_column='SubscriberId', blank=True, null=True)  # Field name made lowercase.
    moadytype = models.SmallIntegerField(db_column='MoadyType', blank=True, null=True)  # Field name made lowercase.
    financegoodtype = models.IntegerField(db_column='FinanceGoodType', blank=True, null=True)  # Field name made lowercase.
    financegoodtypetitle = models.CharField(db_column='FinanceGoodTypeTitle', max_length=100, blank=True, null=True)  # Field name made lowercase.
    deliveryplaceid = models.IntegerField(db_column='DeliveryPlaceId', blank=True, null=True)  # Field name made lowercase.
    deliveryprice = models.DecimalField(db_column='DeliveryPrice', max_digits=23, decimal_places=9)  # Field name made lowercase.
    branchcode = models.CharField(db_column='BranchCode', max_length=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PerInf'


class Permission(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=50)  # Field name made lowercase.
    englishtitle = models.CharField(db_column='EnglishTitle', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Permission'


class Personbgprd(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    personcode = models.IntegerField(db_column='PersonCode')  # Field name made lowercase.
    currencycode = models.IntegerField(db_column='CurrencyCode')  # Field name made lowercase.
    currencyrate = models.DecimalField(db_column='CurrencyRate', max_digits=23, decimal_places=8)  # Field name made lowercase.
    amount = models.DecimalField(db_column='Amount', max_digits=23, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    sitbgprd = models.SmallIntegerField(db_column='sitBgPrd')  # Field name made lowercase.
    comment = models.CharField(db_column='Comment', max_length=500, blank=True, null=True)  # Field name made lowercase.
    tmp = models.SmallIntegerField()
    radif = models.IntegerField(db_column='Radif', blank=True, null=True)  # Field name made lowercase.
    createby = models.CharField(db_column='CreateBy', max_length=100, blank=True, null=True)  # Field name made lowercase.
    createdate = models.DateTimeField(db_column='CreateDate', blank=True, null=True)  # Field name made lowercase.
    modifyby = models.CharField(db_column='ModifyBy', max_length=100, blank=True, null=True)  # Field name made lowercase.
    modifydate = models.DateTimeField(db_column='ModifyDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PersonBgPrd'


class PersonAddresses(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    radif = models.IntegerField(db_column='Radif')  # Field name made lowercase.
    personcode = models.IntegerField(db_column='PersonCode')  # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=100)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=500, blank=True, null=True)  # Field name made lowercase.
    citycode = models.IntegerField(db_column='CityCode', blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=500, blank=True, null=True)  # Field name made lowercase.
    tel = models.CharField(db_column='Tel', max_length=15, blank=True, null=True)  # Field name made lowercase.
    mobile = models.CharField(db_column='Mobile', max_length=15, blank=True, null=True)  # Field name made lowercase.
    postalcode = models.CharField(db_column='PostalCode', max_length=10, blank=True, null=True)  # Field name made lowercase.
    latitude = models.DecimalField(db_column='Latitude', max_digits=23, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    longitude = models.DecimalField(db_column='Longitude', max_digits=23, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    tmp = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'Person_Addresses'


class PersonCategory(models.Model):
    id = id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    person_code = models.IntegerField(db_column='Person_code', blank=True, null=True)  # Field name made lowercase.
    category_code = models.IntegerField(db_column='Category_code')  # Field name made lowercase.
    tmp = models.IntegerField(db_column='Tmp')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Person_category'


class Phonebook(models.Model):
    fname = models.CharField(max_length=50, blank=True, null=True)
    lname = models.CharField(max_length=100, blank=True, null=True)
    tel1 = models.CharField(max_length=50, blank=True, null=True)
    tel2 = models.CharField(max_length=50, blank=True, null=True)
    fax = models.CharField(max_length=50, blank=True, null=True)
    mobile = models.CharField(max_length=50, blank=True, null=True)
    company = models.CharField(max_length=50, blank=True, null=True)
    address1 = models.CharField(max_length=300, blank=True, null=True)
    address2 = models.CharField(max_length=300, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    comment = models.CharField(max_length=500, blank=True, null=True)
    id = id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    code = models.IntegerField(blank=True, null=True)
    identifier = models.CharField(db_column='Identifier', max_length=50, blank=True, null=True)  # Field name made lowercase.
    respect = models.CharField(db_column='Respect', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Phonebook'


class Photogallery(models.Model):
    code = models.IntegerField(db_column='Code')  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=500, blank=True, null=True)  # Field name made lowercase.
    comment = models.CharField(db_column='Comment', max_length=500, blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=300, blank=True, null=True)  # Field name made lowercase.
    picture = models.BinaryField(db_column='Picture', blank=True, null=True)  # Field name made lowercase.
    date_pic = models.CharField(max_length=10, blank=True, null=True)
    tree_code = models.IntegerField(db_column='Tree_code', blank=True, null=True)  # Field name made lowercase.
    checkforonlinemarket = models.BooleanField(db_column='CheckForOnlineMarket')  # Field name made lowercase.
    hash = models.CharField(db_column='Hash', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PhotoGallery'


class Photogallerydetail(models.Model):
    id = models.IntegerField(primary_key=True, db_comment='کليد اصلي جدول')
    codephotogalleryref = models.IntegerField(db_column='CodePhotoGalleryRef', db_comment='کليد فرعي ارتباط با جدول گالري')  # Field name made lowercase.
    typeref = models.SmallIntegerField(db_column='typeRef', db_comment='نوع(شخص،کالا، اسناد...)')  # Field name made lowercase.
    coderef = models.IntegerField(db_column='CodeRef', db_comment='کليد جدول متناسب با نوع')  # Field name made lowercase.
    codedetref = models.IntegerField(db_column='CodeDetRef', blank=True, null=True, db_comment='کليد جزء جدول متناسب با نوع')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PhotoGalleryDetail'


class Pishforoosh(models.Model):
    code = models.IntegerField(db_column='Code', primary_key=True)  # Field name made lowercase.
    shakhs_code = models.IntegerField(db_column='Shakhs_Code', blank=True, null=True)  # Field name made lowercase.
    tavasot = models.CharField(max_length=50, blank=True, null=True)
    tarikh = models.CharField(max_length=50, blank=True, null=True)
    mablagh_factor = models.DecimalField(max_digits=23, decimal_places=9, blank=True, null=True)
    sharh = models.CharField(max_length=500, blank=True, null=True)
    status = models.SmallIntegerField(blank=True, null=True)
    com_index = models.IntegerField(db_column='Com_Index')  # Field name made lowercase.
    extname = models.CharField(db_column='ExtName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    charge = models.DecimalField(db_column='Charge', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    tax = models.DecimalField(db_column='Tax', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    takhfif = models.DecimalField(db_column='Takhfif', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    changetosell = models.BooleanField(db_column='ChangeToSell', blank=True, null=True)  # Field name made lowercase.
    changetobuy = models.BooleanField(db_column='ChangeToBuy', blank=True, null=True)  # Field name made lowercase.
    visitor_code = models.IntegerField(db_column='Visitor_Code', blank=True, null=True)  # Field name made lowercase.
    refrenceid = models.CharField(db_column='RefrenceID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    takhfif_type = models.BooleanField(db_column='Takhfif_Type', blank=True, null=True)  # Field name made lowercase.
    takhfif_percent = models.DecimalField(db_column='Takhfif_Percent', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    deliverydate = models.CharField(db_column='DeliveryDate', max_length=10, blank=True, null=True)  # Field name made lowercase.
    addrtitle = models.CharField(db_column='ADDRTITLE', max_length=100, blank=True, null=True)  # Field name made lowercase.
    addrdescription = models.CharField(db_column='ADDRDESCRIPTION', max_length=500, blank=True, null=True)  # Field name made lowercase.
    addrcitycode = models.IntegerField(db_column='ADDRCITYCODE', blank=True, null=True)  # Field name made lowercase.
    addraddress = models.CharField(db_column='ADDRADDRESS', max_length=500, blank=True, null=True)  # Field name made lowercase.
    addrtel = models.CharField(db_column='ADDRTEL', max_length=15, blank=True, null=True)  # Field name made lowercase.
    addrmobile = models.CharField(db_column='ADDRMOBILE', max_length=15, blank=True, null=True)  # Field name made lowercase.
    addrpostalcode = models.CharField(db_column='ADDRPOSTALCODE', max_length=10, blank=True, null=True)  # Field name made lowercase.
    addrlatitude = models.DecimalField(db_column='ADDRLATITUDE', max_digits=23, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    addrlongitude = models.DecimalField(db_column='ADDRLONGITUDE', max_digits=23, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    createdtime = models.CharField(db_column='CreatedTime', max_length=5)  # Field name made lowercase.
    createddate = models.CharField(db_column='CreatedDate', max_length=10)  # Field name made lowercase.
    modifiedtime = models.CharField(db_column='ModifiedTime', max_length=5, blank=True, null=True)  # Field name made lowercase.
    modifieddate = models.CharField(db_column='ModifiedDate', max_length=10, blank=True, null=True)  # Field name made lowercase.
    usercreated = models.IntegerField(db_column='UserCreated')  # Field name made lowercase.
    usermodified = models.IntegerField(db_column='UserModified', blank=True, null=True)  # Field name made lowercase.
    owner = models.IntegerField(db_column='Owner')  # Field name made lowercase.
    changetoorder = models.BooleanField(db_column='ChangeToOrder')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PishForoosh'


class PishforooshDetail(models.Model):
    code = models.IntegerField(primary_key=True)  # The composite primary key (code, radif) found, that is not supported. The first column is selected.
    radif = models.SmallIntegerField()
    an_code = models.SmallIntegerField(blank=True, null=True)
    kala_code = models.IntegerField(blank=True, null=True)
    sharh = models.CharField(max_length=500, blank=True, null=True)
    meghdar = models.DecimalField(max_digits=23, decimal_places=8, blank=True, null=True)
    naghdi = models.DecimalField(max_digits=23, decimal_places=9, blank=True, null=True)
    reval = models.IntegerField(blank=True, null=True)
    vaziyat = models.SmallIntegerField(blank=True, null=True)
    status = models.SmallIntegerField(blank=True, null=True)
    tool = models.DecimalField(max_digits=23, decimal_places=8, blank=True, null=True)
    arz = models.DecimalField(max_digits=23, decimal_places=8, blank=True, null=True)
    tedad = models.IntegerField(blank=True, null=True)
    meghdar2 = models.DecimalField(max_digits=23, decimal_places=8, blank=True, null=True)
    ghotr = models.DecimalField(max_digits=23, decimal_places=8, blank=True, null=True)
    com_index = models.IntegerField()
    userprice = models.DecimalField(db_column='UserPrice', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    chargepercent = models.DecimalField(db_column='ChargePercent', max_digits=23, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    taxpercent = models.DecimalField(db_column='TaxPercent', max_digits=23, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    takhfif = models.DecimalField(db_column='Takhfif', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    takhfif_costtype = models.BooleanField(db_column='Takhfif_CostType', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PishForoosh_Detail'
        unique_together = (('code', 'radif'),)


class Posinf(models.Model):
    name_bank = models.CharField(db_column='Name_bank', max_length=100)  # Field name made lowercase.
    code_bank = models.IntegerField(db_column='Code_bank')  # Field name made lowercase.
    port = models.CharField(db_column='Port', max_length=50, blank=True, null=True)  # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=160, blank=True, null=True)  # Field name made lowercase.
    comment = models.CharField(max_length=200, blank=True, null=True)
    auto = models.BooleanField(db_column='Auto', blank=True, null=True)  # Field name made lowercase.
    terminalnumber = models.CharField(db_column='TerminalNumber', max_length=20, blank=True, null=True)  # Field name made lowercase.
    pos_type = models.CharField(max_length=20, blank=True, null=True)
    serial = models.CharField(db_column='Serial', max_length=50, blank=True, null=True)  # Field name made lowercase.
    terminal = models.CharField(db_column='Terminal', max_length=20, blank=True, null=True)  # Field name made lowercase.
    acceptor = models.CharField(db_column='Acceptor', max_length=20, blank=True, null=True)  # Field name made lowercase.
    usecounter = models.SmallIntegerField(db_column='UseCounter', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PosInf'


class Prdformulagroup(models.Model):
    code = models.IntegerField(db_column='Code', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=100, blank=True, null=True)  # Field name made lowercase.
    comment = models.CharField(db_column='Comment', max_length=500, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PrdFormulaGroup'


class Prdgoods(models.Model):
    code = models.SmallIntegerField(db_column='Code', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=50, blank=True, null=True)  # Field name made lowercase.
    comment = models.CharField(db_column='Comment', max_length=500, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PrdGoods'


class PrintEstimationCost(models.Model):
    id = models.IntegerField(db_column='ID',primary_key=True)  # Field name made lowercase.
    produceformulacode = models.IntegerField(db_column='ProduceFormulaCode')  # Field name made lowercase.
    type = models.SmallIntegerField(db_column='Type')  # Field name made lowercase.
    costcode = models.IntegerField(db_column='CostCode')  # Field name made lowercase.
    cost = models.DecimalField(db_column='Cost', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    comment = models.CharField(db_column='Comment', max_length=500, blank=True, null=True)  # Field name made lowercase.
    tmp = models.SmallIntegerField()
    costname = models.CharField(db_column='CostName', max_length=151, blank=True, null=True)  # Field name made lowercase.
    costtypename = models.CharField(db_column='CostTypeName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    comindex = models.IntegerField(db_column='ComIndex')  # Field name made lowercase.
    totalcost = models.DecimalField(db_column='TotalCost', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Print_Estimation_Cost'


class PrintEstimationGood(models.Model):
    id = models.IntegerField(db_column='ID',primary_key=True)  # Field name made lowercase.
    produceformulacode = models.IntegerField(db_column='ProduceFormulaCode')  # Field name made lowercase.
    goodcode = models.IntegerField(db_column='GoodCode')  # Field name made lowercase.
    amount = models.DecimalField(db_column='Amount', max_digits=23, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    comment = models.CharField(db_column='Comment', max_length=500, blank=True, null=True)  # Field name made lowercase.
    tmp = models.SmallIntegerField()
    goodname = models.CharField(db_column='GoodName', max_length=153, blank=True, null=True)  # Field name made lowercase.
    unitname = models.CharField(db_column='UnitName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    comindex = models.IntegerField(db_column='ComIndex')  # Field name made lowercase.
    cost = models.DecimalField(db_column='Cost', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    totalcost = models.DecimalField(db_column='TotalCost', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    totalamount = models.DecimalField(db_column='TotalAmount', max_digits=23, decimal_places=8, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Print_Estimation_Good'


class Printssettings(models.Model):
    partname = models.CharField(db_column='PartName', primary_key=True, max_length=20)  # Field name made lowercase. The composite primary key (PartName, TypeName, ManageType, UserCode) found, that is not supported. The first column is selected.
    typename = models.CharField(db_column='TypeName', max_length=300)  # Field name made lowercase.
    comment = models.CharField(db_column='Comment', max_length=500, blank=True, null=True)  # Field name made lowercase.
    meghdar = models.DecimalField(db_column='Meghdar', max_digits=23, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    managetype = models.SmallIntegerField(db_column='ManageType')  # Field name made lowercase.
    usercode = models.IntegerField(db_column='UserCode')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PrintsSettings'
        unique_together = (('partname', 'typename', 'managetype', 'usercode'),)


class Produceformula(models.Model):
    code = models.IntegerField(db_column='Code', primary_key=True)  # Field name made lowercase.
    productcode = models.IntegerField(db_column='ProductCode')  # Field name made lowercase.
    costtype = models.SmallIntegerField(db_column='CostType')  # Field name made lowercase.
    producetime = models.CharField(db_column='ProduceTime', max_length=5, blank=True, null=True)  # Field name made lowercase.
    goodstorecode = models.IntegerField(db_column='GoodStoreCode', blank=True, null=True)  # Field name made lowercase.
    productstorecode = models.IntegerField(db_column='ProductStoreCode', blank=True, null=True)  # Field name made lowercase.
    comment = models.CharField(db_column='Comment', max_length=500, blank=True, null=True)  # Field name made lowercase.
    modifieddate = models.CharField(db_column='ModifiedDate', max_length=10)  # Field name made lowercase.
    benefitcode = models.IntegerField(db_column='BenefitCode', blank=True, null=True)  # Field name made lowercase.
    producedetail = models.TextField(db_column='ProduceDetail', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    grpcode = models.IntegerField(db_column='GrpCode')  # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=100, blank=True, null=True)  # Field name made lowercase.
    producecount = models.DecimalField(db_column='ProduceCount', max_digits=23, decimal_places=8, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ProduceFormula'


class Produceformulacost(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    produceformulacode = models.IntegerField(db_column='ProduceFormulaCode')  # Field name made lowercase.
    type = models.SmallIntegerField(db_column='Type')  # Field name made lowercase.
    costcode = models.IntegerField(db_column='CostCode')  # Field name made lowercase.
    cost = models.DecimalField(db_column='Cost', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    comment = models.CharField(db_column='Comment', max_length=500, blank=True, null=True)  # Field name made lowercase.
    tmp = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'ProduceFormulaCost'


class Produceformulagood(models.Model):
    produceformulacode = models.IntegerField(db_column='ProduceFormulaCode')  # Field name made lowercase.
    goodcode = models.IntegerField(db_column='GoodCode')  # Field name made lowercase.
    amount = models.DecimalField(db_column='Amount', max_digits=23, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    comment = models.CharField(db_column='Comment', max_length=500, blank=True, null=True)  # Field name made lowercase.
    tmp = models.SmallIntegerField()
    amount2 = models.DecimalField(db_column='Amount2', max_digits=23, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    id = models.IntegerField(db_column='ID', blank=True, primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ProduceFormulaGood'


class Productionestimate(models.Model):
    id = id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    formulacode = models.IntegerField(db_column='FormulaCode')  # Field name made lowercase.
    productcode = models.IntegerField(db_column='ProductCode')  # Field name made lowercase.
    time = models.CharField(db_column='Time', max_length=5, blank=True, null=True)  # Field name made lowercase.
    amount = models.DecimalField(db_column='Amount', max_digits=23, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    cost = models.DecimalField(db_column='Cost', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    productioncost = models.DecimalField(db_column='ProductionCost', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    averagecost = models.DecimalField(db_column='AverageCost', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    lastbuycost = models.DecimalField(db_column='LastBuyCost', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    costtype = models.SmallIntegerField(db_column='CostType')  # Field name made lowercase.
    checked = models.BooleanField(db_column='Checked')  # Field name made lowercase.
    com_index = models.IntegerField(db_column='Com_Index')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ProductionEstimate'


class Projects(models.Model):
    code = models.IntegerField(db_column='Code', primary_key=True)  # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=100, blank=True, null=True)  # Field name made lowercase.
    tafsili2 = models.IntegerField(unique=True)
    comment = models.CharField(db_column='Comment', max_length=250, blank=True, null=True)  # Field name made lowercase.
    parent_code = models.IntegerField(db_column='Parent_Code', blank=True, null=True)  # Field name made lowercase.
    level_code = models.IntegerField(db_column='Level_Code', blank=True, null=True)  # Field name made lowercase.
    projectcrn = models.CharField(db_column='ProjectCRN', max_length=12, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Projects'
        unique_together = (('tafsili2', 'title'),)


class Promotion(models.Model):
    codepromotion = models.IntegerField(db_column='CodePromotion', primary_key=True)  # Field name made lowercase.
    namepromotion = models.CharField(db_column='NamePromotion', max_length=500)  # Field name made lowercase.
    prioritypromotion = models.SmallIntegerField(db_column='PriorityPromotion')  # Field name made lowercase.
    datestart = models.CharField(db_column='DateStart', max_length=10)  # Field name made lowercase.
    dateend = models.CharField(db_column='DateEnd', max_length=10)  # Field name made lowercase.
    timestart = models.CharField(db_column='TimeStart', max_length=5)  # Field name made lowercase.
    timeend = models.CharField(db_column='TimeEnd', max_length=5)  # Field name made lowercase.
    levelpromotion = models.SmallIntegerField(db_column='LevelPromotion')  # Field name made lowercase.
    accordingto = models.SmallIntegerField(db_column='AccordingTo')  # Field name made lowercase.
    iscalclinear = models.BooleanField(db_column='IsCalcLinear')  # Field name made lowercase.
    factorquery = models.TextField(db_column='FactorQuery', blank=True, null=True)  # Field name made lowercase.
    customerquery = models.TextField(db_column='CustomerQuery', blank=True, null=True)  # Field name made lowercase.
    goodquery = models.TextField(db_column='GoodQuery', blank=True, null=True)  # Field name made lowercase.
    visitorquery = models.TextField(db_column='VisitorQuery', blank=True, null=True)  # Field name made lowercase.
    typetasvieh = models.SmallIntegerField(db_column='TypeTasvieh', blank=True, null=True)  # Field name made lowercase.
    deadlinetasvieh = models.SmallIntegerField(db_column='DeadlineTasvieh', blank=True, null=True)  # Field name made lowercase.
    isactive = models.BooleanField(db_column='IsActive')  # Field name made lowercase.
    despromotion = models.CharField(db_column='DesPromotion', max_length=500, blank=True, null=True)  # Field name made lowercase.
    isallcustomer = models.BooleanField(db_column='IsAllCustomer')  # Field name made lowercase.
    isallvisitor = models.BooleanField(db_column='IsAllVisitor')  # Field name made lowercase.
    isallgood = models.BooleanField(db_column='IsAllGood')  # Field name made lowercase.
    isallservice = models.BooleanField(db_column='IsAllService')  # Field name made lowercase.
    isallanbar = models.BooleanField(db_column='IsAllAnbar')  # Field name made lowercase.
    aggregatewithother = models.SmallIntegerField(db_column='AggregateWithOther', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Promotion'


class Promotionanbar(models.Model):
    codepromotionanbar = models.AutoField(db_column='CodePromotionAnbar', primary_key=True)  # Field name made lowercase.
    codeanbar = models.IntegerField(db_column='CodeAnbar')  # Field name made lowercase.
    codepromotion = models.IntegerField(db_column='CodePromotion')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PromotionAnbar'


class Promotioncustomer(models.Model):
    codepromotioncustomer = models.AutoField(db_column='CodePromotionCustomer', primary_key=True)  # Field name made lowercase.
    codecustomer = models.ForeignKey(Perinf, on_delete=models.DO_NOTHING, db_column='CodeCustomer')  # Field name made lowercase.
    codepromotion = models.ForeignKey(Promotion, on_delete=models.DO_NOTHING, db_column='CodePromotion')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PromotionCustomer'


class Promotioncustomergroup(models.Model):
    codepromotioncustomergroup = models.AutoField(db_column='CodePromotionCustomerGroup', primary_key=True)  # Field name made lowercase.
    codecustomergroup = models.IntegerField(db_column='CodeCustomerGroup')  # Field name made lowercase.
    codepromotion = models.ForeignKey(Promotion, on_delete=models.DO_NOTHING, db_column='CodePromotion')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PromotionCustomerGroup'


class Promotiongood(models.Model):
    codepromotiongood = models.AutoField(db_column='CodePromotionGood', primary_key=True)  # Field name made lowercase.
    codegood = models.ForeignKey(Goodinf, on_delete=models.DO_NOTHING, db_column='CodeGood')  # Field name made lowercase.
    codepromotion = models.ForeignKey(Promotion, on_delete=models.DO_NOTHING, db_column='CodePromotion')  # Field name made lowercase.
    type = models.SmallIntegerField(db_column='Type')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PromotionGood'
        unique_together = (('codegood', 'codepromotion', 'type'),)


class Promotiongoodgroup(models.Model):
    codepromotiongoodgroup = models.AutoField(db_column='CodePromotionGoodGroup', primary_key=True)  # Field name made lowercase.
    codegoodgroup = models.IntegerField(db_column='CodeGoodGroup')  # Field name made lowercase.
    codepromotion = models.ForeignKey(Promotion, on_delete=models.DO_NOTHING, db_column='CodePromotion')  # Field name made lowercase.
    type = models.SmallIntegerField(db_column='Type')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PromotionGoodGroup'


class Promotionorderfromgood(models.Model):
    codepromotionorderfromgood = models.AutoField(db_column='CodePromotionOrderFromGood', primary_key=True)  # Field name made lowercase.
    codegood = models.IntegerField(db_column='CodeGood')  # Field name made lowercase.
    codepromotion = models.ForeignKey(Promotion, on_delete=models.DO_NOTHING, db_column='CodePromotion')  # Field name made lowercase.
    meghdargood = models.DecimalField(db_column='MeghdarGood', max_digits=23, decimal_places=8)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PromotionOrderFromGood'


class Promotiontypetasvieh(models.Model):
    codetypetasvieh = models.SmallAutoField(db_column='CodeTypeTasvieh', primary_key=True)  # Field name made lowercase.
    nametypetasvieh = models.CharField(db_column='NameTypeTasvieh', max_length=1000)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PromotionTypeTasvieh'


class Promotionvisitor(models.Model):
    codepromotionvisitor = models.AutoField(db_column='CodePromotionVisitor', primary_key=True)  # Field name made lowercase.
    codevisitor = models.ForeignKey(Perinf, on_delete=models.DO_NOTHING, db_column='CodeVisitor')  # Field name made lowercase.
    codepromotion = models.ForeignKey(Promotion, on_delete=models.DO_NOTHING, db_column='CodePromotion')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PromotionVisitor'


class PromotionDet(models.Model):
    codepromotion_det = models.AutoField(db_column='CodePromotion_Det', primary_key=True)  # Field name made lowercase.
    codepromotion = models.ForeignKey(Promotion, on_delete=models.DO_NOTHING, db_column='CodePromotion')  # Field name made lowercase.
    howtopromotion = models.SmallIntegerField(db_column='HowToPromotion')  # Field name made lowercase.
    iscalcadditive = models.BooleanField(db_column='IsCalcAdditive')  # Field name made lowercase.
    reducedeffectonprice = models.BooleanField(db_column='ReducedEffectOnPrice')  # Field name made lowercase.
    topayment = models.DecimalField(db_column='ToPayment', max_digits=23, decimal_places=9)  # Field name made lowercase.
    meghdarpromotion = models.DecimalField(db_column='MeghdarPromotion', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    an_code = models.SmallIntegerField(blank=True, null=True)
    codegood = models.IntegerField(db_column='CodeGood', blank=True, null=True)  # Field name made lowercase.
    tool = models.DecimalField(max_digits=23, decimal_places=9, blank=True, null=True)
    arz = models.DecimalField(max_digits=23, decimal_places=9, blank=True, null=True)
    tedad = models.IntegerField(blank=True, null=True)
    meghdar2 = models.DecimalField(max_digits=23, decimal_places=9, blank=True, null=True)
    ghotr = models.DecimalField(max_digits=23, decimal_places=9, blank=True, null=True)
    toolidcode = models.IntegerField(db_column='ToolidCode', blank=True, null=True)  # Field name made lowercase.
    meghdar = models.DecimalField(max_digits=23, decimal_places=8, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Promotion_Det'


class Questionkeys(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    questioncode = models.ForeignKey('Questions', on_delete=models.DO_NOTHING, db_column='QuestionCode')  # Field name made lowercase.
    keycount = models.IntegerField(db_column='KeyCount', blank=True, null=True)  # Field name made lowercase.
    keys = models.CharField(db_column='Keys', max_length=4000, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'QuestionKeys'


class Questions(models.Model):
    id = id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    code = models.IntegerField(db_column='Code')  # Field name made lowercase.
    answercode = models.ForeignKey(Answers, on_delete=models.DO_NOTHING, db_column='AnswerCode', blank=True, null=True)  # Field name made lowercase.
    question = models.CharField(db_column='Question', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    softwarepart = models.IntegerField(db_column='SoftwarePart', blank=True, null=True)  # Field name made lowercase.
    feature = models.IntegerField(db_column='Feature', blank=True, null=True)  # Field name made lowercase.
    softwaretype = models.IntegerField(db_column='SoftwareType', blank=True, null=True)  # Field name made lowercase.
    creatdate = models.DateTimeField(db_column='CreatDate', blank=True, null=True)  # Field name made lowercase.
    modifydate = models.DateTimeField(db_column='ModifyDate', blank=True, null=True)  # Field name made lowercase.
    subject = models.CharField(db_column='Subject', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Questions'


class RsAccessories(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=100)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RS_Accessories'


class RsCostServices(models.Model):
    service_id = models.IntegerField(db_column='Service_ID', primary_key=True)  # Field name made lowercase.
    cost = models.DecimalField(db_column='Cost', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    techcost = models.DecimalField(db_column='TechCost', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RS_Cost_Services'


class RsCustomers(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    prefix = models.CharField(db_column='Prefix', max_length=20, blank=True, null=True)  # Field name made lowercase.
    firstname = models.CharField(db_column='FirstName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    lastname = models.CharField(db_column='LastName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    tel = models.CharField(db_column='Tel', max_length=50, blank=True, null=True)  # Field name made lowercase.
    mobile = models.CharField(db_column='Mobile', max_length=50, blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=300, blank=True, null=True)  # Field name made lowercase.
    flag = models.IntegerField(db_column='Flag', blank=True, null=True)  # Field name made lowercase.
    group_id = models.IntegerField(db_column='Group_ID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RS_Customers'


class RsProblems(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=100)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RS_Problems'


class RsServiceAccessories(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    service = models.ForeignKey('RsServiceEnterance', on_delete=models.DO_NOTHING, db_column='Service_ID')  # Field name made lowercase.
    accessory = models.ForeignKey(RsAccessories, on_delete=models.DO_NOTHING, db_column='Accessory_ID')  # Field name made lowercase.
    edit_flag = models.SmallIntegerField(db_column='Edit_Flag')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RS_Service_Accessories'


class RsServiceEnterance(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    reciept_id = models.CharField(db_column='Reciept_ID', max_length=10)  # Field name made lowercase.
    customer_id = models.IntegerField(db_column='Customer_ID')  # Field name made lowercase.
    date = models.CharField(db_column='Date', max_length=10)  # Field name made lowercase.
    device_type = models.CharField(db_column='Device_Type', max_length=50)  # Field name made lowercase.
    device_model = models.CharField(db_column='Device_Model', max_length=50, blank=True, null=True)  # Field name made lowercase.
    device_serial = models.CharField(db_column='Device_Serial', max_length=50, blank=True, null=True)  # Field name made lowercase.
    estimate_finish_date = models.CharField(db_column='Estimate_Finish_Date', max_length=10)  # Field name made lowercase.
    garranty_status = models.BooleanField(db_column='Garranty_Status')  # Field name made lowercase.
    comment = models.CharField(db_column='Comment', max_length=500, blank=True, null=True)  # Field name made lowercase.
    garranty_date = models.CharField(db_column='Garranty_Date', max_length=10, blank=True, null=True)  # Field name made lowercase.
    estimate_cost = models.DecimalField(db_column='Estimate_Cost', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    current_state = models.SmallIntegerField(db_column='Current_State')  # Field name made lowercase.
    device_brand = models.CharField(db_column='Device_Brand', max_length=50, blank=True, null=True)  # Field name made lowercase.
    guarantee_id = models.IntegerField(db_column='Guarantee_ID', blank=True, null=True)  # Field name made lowercase.
    sell_id = models.IntegerField(db_column='Sell_ID', blank=True, null=True)  # Field name made lowercase.
    rowtype = models.SmallIntegerField(db_column='RowType', blank=True, null=True)  # Field name made lowercase.
    rowid = models.IntegerField(db_column='RowID', blank=True, null=True)  # Field name made lowercase.
    repair_comment = models.CharField(db_column='Repair_Comment', max_length=500, blank=True, null=True)  # Field name made lowercase.
    repair_state = models.BooleanField(db_column='Repair_State', blank=True, null=True)  # Field name made lowercase.
    delivery_date = models.CharField(db_column='Delivery_Date', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RS_Service_Enterance'


class RsServiceProblems(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    service = models.ForeignKey(RsServiceEnterance, on_delete=models.DO_NOTHING, db_column='Service_ID')  # Field name made lowercase.
    problem = models.ForeignKey(RsProblems, on_delete=models.DO_NOTHING, db_column='Problem_ID')  # Field name made lowercase.
    edit_flag = models.SmallIntegerField(db_column='Edit_Flag')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RS_Service_Problems'


class RsServiceTechnision(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    enterance = models.ForeignKey(RsServiceEnterance, on_delete=models.DO_NOTHING, db_column='Enterance_ID')  # Field name made lowercase.
    technision_id = models.IntegerField(db_column='Technision_ID', blank=True, null=True)  # Field name made lowercase.
    date = models.CharField(db_column='Date', max_length=10)  # Field name made lowercase.
    comment = models.CharField(db_column='Comment', max_length=2000, blank=True, null=True)  # Field name made lowercase.
    end_date = models.CharField(db_column='End_Date', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RS_Service_Technision'


class RsSettings(models.Model):
    code = models.IntegerField(db_column='Code', primary_key=True)  # Field name made lowercase.
    text_value = models.CharField(db_column='Text_Value', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    number_value = models.DecimalField(db_column='Number_Value', max_digits=23, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    boolean_value = models.BooleanField(db_column='Boolean_Value', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RS_Settings'


class RsTechnisionComponents(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    parent = models.ForeignKey(RsServiceTechnision, on_delete=models.DO_NOTHING, db_column='Parent_ID')  # Field name made lowercase.
    component_id = models.IntegerField(db_column='Component_ID')  # Field name made lowercase.
    amount = models.DecimalField(db_column='Amount', max_digits=23, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    store_id = models.IntegerField(db_column='Store_ID', blank=True, null=True)  # Field name made lowercase.
    cost = models.DecimalField(db_column='Cost', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    discount = models.DecimalField(db_column='Discount', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    charge = models.DecimalField(db_column='Charge', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    tax = models.DecimalField(db_column='Tax', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    grnt_status = models.BooleanField(db_column='GRNT_Status', blank=True, null=True)  # Field name made lowercase.
    grnt_id = models.IntegerField(db_column='GRNT_ID', blank=True, null=True)  # Field name made lowercase.
    grnt_startdate_type = models.SmallIntegerField(db_column='GRNT_StartDate_Type', blank=True, null=True)  # Field name made lowercase.
    grnt_startdate = models.CharField(db_column='GRNT_StartDate', max_length=10, blank=True, null=True)  # Field name made lowercase.
    grnt_year = models.SmallIntegerField(db_column='GRNT_Year', blank=True, null=True)  # Field name made lowercase.
    grnt_month = models.SmallIntegerField(db_column='GRNT_Month', blank=True, null=True)  # Field name made lowercase.
    grnt_day = models.SmallIntegerField(db_column='GRNT_Day', blank=True, null=True)  # Field name made lowercase.
    comment = models.CharField(db_column='Comment', max_length=500, blank=True, null=True)  # Field name made lowercase.
    status = models.SmallIntegerField(db_column='Status', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RS_Technision_Components'


class RsTechnisionServices(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    parent = models.ForeignKey(RsServiceTechnision, on_delete=models.DO_NOTHING, db_column='Parent_ID')  # Field name made lowercase.
    service_id = models.IntegerField(db_column='Service_ID')  # Field name made lowercase.
    amount = models.DecimalField(db_column='Amount', max_digits=23, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    cost = models.DecimalField(db_column='Cost', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    discount = models.DecimalField(db_column='Discount', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    charge = models.DecimalField(db_column='Charge', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    tax = models.DecimalField(db_column='Tax', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    grnt_status = models.BooleanField(db_column='GRNT_Status', blank=True, null=True)  # Field name made lowercase.
    grnt_id = models.IntegerField(db_column='GRNT_ID', blank=True, null=True)  # Field name made lowercase.
    grnt_year = models.SmallIntegerField(db_column='GRNT_Year', blank=True, null=True)  # Field name made lowercase.
    grnt_month = models.SmallIntegerField(db_column='GRNT_Month', blank=True, null=True)  # Field name made lowercase.
    grnt_day = models.SmallIntegerField(db_column='GRNT_Day', blank=True, null=True)  # Field name made lowercase.
    comment = models.CharField(db_column='Comment', max_length=500, blank=True, null=True)  # Field name made lowercase.
    wage = models.DecimalField(db_column='Wage', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    technision_id = models.IntegerField(db_column='Technision_ID', blank=True, null=True)  # Field name made lowercase.
    status = models.SmallIntegerField(db_column='Status', blank=True, null=True)  # Field name made lowercase.
    wage_type = models.SmallIntegerField(db_column='Wage_Type', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RS_Technision_Services'


class Rasgiri(models.Model):
    date = models.CharField(db_column='Date', max_length=10, blank=True, null=True)  # Field name made lowercase.
    comment = models.CharField(db_column='Comment', max_length=500, blank=True, null=True)  # Field name made lowercase.
    daynum = models.IntegerField(db_column='DayNum', blank=True, null=True)  # Field name made lowercase.
    bed = models.DecimalField(db_column='Bed', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    bes = models.DecimalField(db_column='Bes', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    type = models.SmallIntegerField(db_column='Type', blank=True, null=True)  # Field name made lowercase.
    radif = models.AutoField(db_column='Radif',primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RasGiri'


class Reasonsforoperations(models.Model):
    reasonid = models.AutoField(db_column='ReasonID', primary_key=True)  # Field name made lowercase.
    code = models.IntegerField(db_column='Code')  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=150, blank=True, null=True)  # Field name made lowercase.
    comment = models.CharField(db_column='Comment', max_length=500, blank=True, null=True)  # Field name made lowercase.
    softwaretype = models.IntegerField(db_column='SoftwareType', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ReasonsForOperations'
        unique_together = (('code', 'softwaretype'),)


class Recdeduction(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    recruitmentcode = models.ForeignKey('Recruitment', on_delete=models.DO_NOTHING, db_column='RecruitmentCode')  # Field name made lowercase.
    itemcode = models.ForeignKey(Deduction, on_delete=models.DO_NOTHING, db_column='ItemCode')  # Field name made lowercase.
    cost = models.DecimalField(db_column='Cost', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RecDeduction'


class Recfinish(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    recruitmentcode = models.ForeignKey('Recruitment', on_delete=models.DO_NOTHING, db_column='RecruitmentCode')  # Field name made lowercase.
    licenceid = models.CharField(db_column='LicenceId', max_length=50, blank=True, null=True)  # Field name made lowercase.
    contractid = models.CharField(db_column='ContractId', max_length=50, blank=True, null=True)  # Field name made lowercase.
    file = models.BinaryField(db_column='File', blank=True, null=True)  # Field name made lowercase.
    comment = models.CharField(db_column='Comment', max_length=500, blank=True, null=True)  # Field name made lowercase.
    filename = models.CharField(db_column='FileName', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RecFinish'


class Recfiscal(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    recruitmentcode = models.ForeignKey('Recruitment', on_delete=models.DO_NOTHING, db_column='RecruitmentCode')  # Field name made lowercase.
    itemcode = models.ForeignKey(Fiscal, on_delete=models.DO_NOTHING, db_column='ItemCode')  # Field name made lowercase.
    cost = models.DecimalField(db_column='Cost', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RecFiscal'


class Receiptdetail(models.Model):
    code = models.IntegerField(db_column='Code', primary_key=True)  # Field name made lowercase. The composite primary key (Code, ReceiptCode) found, that is not supported. The first column is selected.
    receiptcode = models.ForeignKey('Receiptgood', on_delete=models.DO_NOTHING, db_column='ReceiptCode')  # Field name made lowercase.
    goodcode = models.IntegerField(db_column='GoodCode', blank=True, null=True)  # Field name made lowercase.
    amount = models.DecimalField(db_column='Amount', max_digits=23, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    amount2 = models.DecimalField(db_column='Amount2', max_digits=23, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    cost = models.DecimalField(db_column='Cost', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    storecode = models.IntegerField(db_column='StoreCode', blank=True, null=True)  # Field name made lowercase.
    comment = models.CharField(db_column='Comment', max_length=500, blank=True, null=True)  # Field name made lowercase.
    width = models.DecimalField(db_column='Width', max_digits=23, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    height = models.DecimalField(db_column='Height', max_digits=23, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    num = models.DecimalField(db_column='Num', max_digits=23, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    global_field = models.ForeignKey(GlobalIds, on_delete=models.DO_NOTHING, db_column='Global_ID', blank=True, null=True)  # Field name made lowercase. Field renamed because it was a Python reserved word.

    class Meta:
        managed = False
        db_table = 'ReceiptDetail'
        unique_together = (('code', 'receiptcode'),)


class Receiptgood(models.Model):
    code = models.IntegerField(db_column='Code', primary_key=True)  # Field name made lowercase.
    detail = models.IntegerField(db_column='Detail', blank=True, null=True)  # Field name made lowercase.
    acctype = models.SmallIntegerField(db_column='AccType', blank=True, null=True)  # Field name made lowercase.
    date = models.CharField(db_column='Date', max_length=10, blank=True, null=True)  # Field name made lowercase.
    lastprintdate = models.CharField(db_column='LastPrintDate', max_length=10, blank=True, null=True)  # Field name made lowercase.
    vouchercode = models.IntegerField(db_column='VoucherCode', blank=True, null=True)  # Field name made lowercase.
    sumcost = models.DecimalField(db_column='SumCost', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    comment = models.CharField(db_column='Comment', max_length=500, blank=True, null=True)  # Field name made lowercase.
    interfacename = models.CharField(db_column='InterfaceName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    isautomatic = models.BooleanField(db_column='IsAutomatic', blank=True, null=True)  # Field name made lowercase.
    total = models.IntegerField(db_column='Total', blank=True, null=True)  # Field name made lowercase.
    assistant = models.IntegerField(db_column='Assistant', blank=True, null=True)  # Field name made lowercase.
    expensecenter = models.IntegerField(db_column='ExpenseCenter', blank=True, null=True)  # Field name made lowercase.
    createdtime = models.CharField(db_column='CreatedTime', max_length=5, blank=True, null=True)  # Field name made lowercase.
    createddate = models.CharField(db_column='CreatedDate', max_length=10, blank=True, null=True)  # Field name made lowercase.
    modifiedtime = models.CharField(db_column='ModifiedTime', max_length=5, blank=True, null=True)  # Field name made lowercase.
    modifieddate = models.CharField(db_column='ModifiedDate', max_length=10, blank=True, null=True)  # Field name made lowercase.
    usercreated = models.IntegerField(db_column='UserCreated')  # Field name made lowercase.
    usermodified = models.IntegerField(db_column='UserModified', blank=True, null=True)  # Field name made lowercase.
    owner = models.IntegerField(db_column='Owner')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ReceiptGood'


class Receiptrelation(models.Model):
    code = models.IntegerField(db_column='Code', primary_key=True)  # Field name made lowercase.
    operationcode = models.IntegerField(db_column='OperationCode', blank=True, null=True)  # Field name made lowercase.
    operationtype = models.SmallIntegerField(db_column='OperationType', blank=True, null=True)  # Field name made lowercase.
    receiptcode = models.ForeignKey(Receiptgood, on_delete=models.DO_NOTHING, db_column='ReceiptCode', blank=True, null=True)  # Field name made lowercase.
    groupcode = models.IntegerField(db_column='GroupCode', blank=True, null=True)  # Field name made lowercase.
    groupstatus = models.BooleanField(db_column='GroupStatus', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ReceiptRelation'


class Reconciliation(models.Model):
    code = models.IntegerField(db_column='Code', primary_key=True, db_comment='کد صورتحساب/مغايرت بانکي')  # Field name made lowercase.
    statementsref = models.ForeignKey('Statements', on_delete=models.DO_NOTHING, db_column='StatementsRef', blank=True, null=True, db_comment='کليد فرعي صورتحساب')  # Field name made lowercase.
    d_start = models.CharField(db_column='D_Start', max_length=10, blank=True, null=True, db_comment='از تاريخ')  # Field name made lowercase.
    d_end = models.CharField(db_column='D_End', max_length=10, blank=True, null=True, db_comment='تا تاريخ')  # Field name made lowercase.
    sitbgprd = models.SmallIntegerField(db_column='SitBgPrd', blank=True, null=True, db_comment='بدهکار/بستانکار')  # Field name made lowercase.
    begininginventory = models.DecimalField(db_column='BeginingInventory', max_digits=23, decimal_places=8, db_comment='موجودي اول دوره')  # Field name made lowercase.
    status = models.SmallIntegerField(db_column='Status', db_comment='وضعيت')  # Field name made lowercase.
    des = models.CharField(db_column='Des', max_length=500, blank=True, null=True, db_comment='شرح')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Reconciliation'


class Reconciliationrelation(models.Model):
    id = models.IntegerField(primary_key=True, db_comment='کليد اصلي')  # The composite primary key (id, IsTemp) found, that is not supported. The first column is selected.
    reconciliationref = models.ForeignKey(Reconciliation, on_delete=models.DO_NOTHING, db_column='ReconciliationRef', blank=True, null=True, db_comment='کليد فرعي مغايرت بانکي')  # Field name made lowercase.
    idmaster = models.IntegerField(db_column='IdMaster', blank=True, null=True, db_comment='کد هم گروه')  # Field name made lowercase.
    idsystemref = models.IntegerField(db_column='IdSystemRef', blank=True, null=True, db_comment='کليد فرعي صورتحساب سيستم')  # Field name made lowercase.
    idbankref = models.IntegerField(db_column='IdBankRef', blank=True, null=True, db_comment='کليد فرعي صورتحساب بانک')  # Field name made lowercase.
    istemp = models.SmallIntegerField(db_column='IsTemp', db_comment='موقت/اصلي')  # Field name made lowercase.
    isautorelation = models.SmallIntegerField(db_column='IsAutoRelation', db_comment='موقت/اصلي')  # Field name made lowercase.
    com_index = models.IntegerField(db_column='Com_Index', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ReconciliationRelation'
        unique_together = (('id', 'istemp'),)


class Recruitment(models.Model):
    code = models.IntegerField(db_column='Code', primary_key=True)  # Field name made lowercase.
    calcmethodcode = models.ForeignKey(Calcmethod, on_delete=models.DO_NOTHING, db_column='CalcMethodCode')  # Field name made lowercase.
    staffcode = models.ForeignKey('Staff', on_delete=models.DO_NOTHING, db_column='StaffCode')  # Field name made lowercase.
    date = models.CharField(db_column='Date', max_length=10)  # Field name made lowercase.
    dodate = models.CharField(db_column='DoDate', max_length=10)  # Field name made lowercase.
    percode = models.ForeignKey(Perinf, on_delete=models.DO_NOTHING, db_column='PerCode', blank=True, null=True)  # Field name made lowercase.
    salary = models.DecimalField(db_column='Salary', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    salarytime = models.DecimalField(db_column='SalaryTime', max_digits=23, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    per_kol = models.IntegerField(db_column='Per_Kol', blank=True, null=True)  # Field name made lowercase.
    per_moin = models.IntegerField(db_column='Per_Moin', blank=True, null=True)  # Field name made lowercase.
    per_tafsili = models.IntegerField(db_column='Per_Tafsili', blank=True, null=True)  # Field name made lowercase.
    createdtime = models.CharField(db_column='CreatedTime', max_length=5, blank=True, null=True)  # Field name made lowercase.
    createddate = models.CharField(db_column='CreatedDate', max_length=10, blank=True, null=True)  # Field name made lowercase.
    modifiedtime = models.CharField(db_column='ModifiedTime', max_length=5, blank=True, null=True)  # Field name made lowercase.
    modifieddate = models.CharField(db_column='ModifiedDate', max_length=10, blank=True, null=True)  # Field name made lowercase.
    usercreated = models.IntegerField(db_column='UserCreated')  # Field name made lowercase.
    usermodified = models.IntegerField(db_column='UserModified', blank=True, null=True)  # Field name made lowercase.
    installment_kol = models.IntegerField(db_column='Installment_Kol', blank=True, null=True)  # Field name made lowercase.
    installment_moin = models.IntegerField(db_column='Installment_Moin', blank=True, null=True)  # Field name made lowercase.
    installment_tafsili = models.IntegerField(db_column='Installment_Tafsili', blank=True, null=True)  # Field name made lowercase.
    installment_percode = models.IntegerField(db_column='Installment_PerCode', blank=True, null=True)  # Field name made lowercase.
    fiscaldeductionupdate = models.BooleanField(db_column='FiscalDeductionUpdate', blank=True, null=True)  # Field name made lowercase.
    owner = models.IntegerField(db_column='Owner')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Recruitment'


class Repairandhold(models.Model):
    code = models.IntegerField(db_column='Code', primary_key=True)  # Field name made lowercase.
    obtaincode = models.IntegerField(db_column='ObtainCode')  # Field name made lowercase.
    date = models.CharField(db_column='Date', max_length=10)  # Field name made lowercase.
    reciever = models.IntegerField(db_column='Reciever')  # Field name made lowercase.
    amount = models.DecimalField(db_column='Amount', max_digits=23, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    comment = models.CharField(db_column='Comment', max_length=500, blank=True, null=True)  # Field name made lowercase.
    vouchercode = models.IntegerField(db_column='VoucherCode', blank=True, null=True)  # Field name made lowercase.
    expcentercode = models.IntegerField(db_column='ExpCenterCode', blank=True, null=True)  # Field name made lowercase.
    createdtime = models.CharField(db_column='CreatedTime', max_length=5)  # Field name made lowercase.
    createddate = models.CharField(db_column='CreatedDate', max_length=10)  # Field name made lowercase.
    modifiedtime = models.CharField(db_column='ModifiedTime', max_length=5, blank=True, null=True)  # Field name made lowercase.
    modifieddate = models.CharField(db_column='ModifiedDate', max_length=10, blank=True, null=True)  # Field name made lowercase.
    usercreated = models.IntegerField(db_column='UserCreated')  # Field name made lowercase.
    usermodified = models.IntegerField(db_column='UserModified', blank=True, null=True)  # Field name made lowercase.
    owner = models.IntegerField(db_column='Owner')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RepairAndHold'


class Repairandholddetail(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    repairandholdcode = models.ForeignKey(Repairandhold, on_delete=models.DO_NOTHING, db_column='RepairAndHoldCode')  # Field name made lowercase.
    expensecode = models.ForeignKey(LHazine, on_delete=models.DO_NOTHING, db_column='ExpenseCode', blank=True, null=True)  # Field name made lowercase.
    expensetype = models.SmallIntegerField(db_column='ExpenseType')  # Field name made lowercase.
    cost = models.DecimalField(db_column='Cost', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    comment = models.CharField(db_column='Comment', max_length=500, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RepairAndHoldDetail'


class Reportfile(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    partcode = models.IntegerField(db_column='PartCode')  # Field name made lowercase.
    printtype = models.SmallIntegerField(db_column='PrintType')  # Field name made lowercase.
    isdefualt = models.BooleanField(db_column='IsDefualt')  # Field name made lowercase.
    printfile = models.BinaryField(db_column='PrintFile')  # Field name made lowercase.
    comment = models.CharField(db_column='Comment', max_length=250, blank=True, null=True)  # Field name made lowercase.
    filename = models.CharField(db_column='FileName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    idreportgroup = models.IntegerField(db_column='IDReportGroup', blank=True, null=True)  # Field name made lowercase.
    userid = models.IntegerField(db_column='UserId', blank=True, null=True)  # Field name made lowercase.
    previewreport = models.BinaryField(db_column='PreviewReport', blank=True, null=True)  # Field name made lowercase.
    filenamepreview = models.CharField(db_column='FileNamePreview', max_length=50, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=250, blank=True, null=True)  # Field name made lowercase.
    templatestype = models.SmallIntegerField(db_column='TemplatesType', blank=True, null=True)  # Field name made lowercase.
    sysprint = models.SmallIntegerField(db_column='SysPrint')  # Field name made lowercase.
    masterid = models.IntegerField(db_column='MasterID', blank=True, null=True)  # Field name made lowercase.
    sqltext = models.TextField(db_column='SqlText', blank=True, null=True)  # Field name made lowercase.
    descriptiontext = models.TextField(db_column='DescriptionText', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ReportFile'


class Reportgroup(models.Model):
    code = models.IntegerField(db_column='Code', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=50)  # Field name made lowercase.
    comment = models.CharField(db_column='Comment', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ReportGroup'


class Reportsprint(models.Model):
    field1 = models.CharField(db_column='Field1', max_length=200, blank=True, null=True)  # Field name made lowercase.
    field2 = models.CharField(db_column='Field2', max_length=100, blank=True, null=True)  # Field name made lowercase.
    field3 = models.CharField(db_column='Field3', max_length=200, blank=True, null=True)  # Field name made lowercase.
    field4 = models.CharField(db_column='Field4', max_length=100, blank=True, null=True)  # Field name made lowercase.
    type = models.SmallIntegerField(db_column='Type', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ReportsPrint'


class Repository(models.Model):
    code = models.IntegerField(db_column='Code', primary_key=True)  # Field name made lowercase.
    grpcode = models.ForeignKey('Repositorygroup', on_delete=models.DO_NOTHING, db_column='GrpCode')  # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=50)  # Field name made lowercase.
    date = models.CharField(db_column='Date', max_length=10)  # Field name made lowercase.
    type = models.SmallIntegerField(db_column='Type', blank=True, null=True)  # Field name made lowercase.
    mastercode = models.IntegerField(db_column='MasterCode', blank=True, null=True)  # Field name made lowercase.
    detailcode = models.IntegerField(db_column='DetailCode', blank=True, null=True)  # Field name made lowercase.
    modifieddate = models.CharField(db_column='ModifiedDate', max_length=10, blank=True, null=True)  # Field name made lowercase.
    usermodified = models.IntegerField(db_column='UserModified', blank=True, null=True)  # Field name made lowercase.
    comment = models.CharField(db_column='Comment', max_length=500, blank=True, null=True)  # Field name made lowercase.
    usercreated = models.IntegerField(db_column='UserCreated')  # Field name made lowercase.
    createdtime = models.CharField(db_column='CreatedTime', max_length=5)  # Field name made lowercase.
    createddate = models.CharField(db_column='CreatedDate', max_length=10)  # Field name made lowercase.
    owner = models.IntegerField(db_column='Owner')  # Field name made lowercase.
    modifiedtime = models.CharField(db_column='ModifiedTime', max_length=5, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Repository'


class Repositorydetail(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    repositorycode = models.ForeignKey(Repository, on_delete=models.DO_NOTHING, db_column='RepositoryCode')  # Field name made lowercase.
    file = models.BinaryField(db_column='File')  # Field name made lowercase.
    fileaddr = models.CharField(db_column='FileAddr', max_length=200)  # Field name made lowercase.
    fileextention = models.CharField(db_column='FileExtention', max_length=5)  # Field name made lowercase.
    comment = models.CharField(db_column='Comment', max_length=500, blank=True, null=True)  # Field name made lowercase.
    holdplace = models.CharField(db_column='HoldPlace', max_length=100, blank=True, null=True)  # Field name made lowercase.
    computername = models.CharField(db_column='ComputerName', max_length=50)  # Field name made lowercase.
    modifieddate = models.CharField(db_column='ModifiedDate', max_length=10)  # Field name made lowercase.
    modifiedtime = models.CharField(db_column='ModifiedTime', max_length=5)  # Field name made lowercase.
    usermodified = models.IntegerField(db_column='UserModified')  # Field name made lowercase.
    type = models.SmallIntegerField(db_column='Type')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RepositoryDetail'


class Repositorygroup(models.Model):
    code = models.IntegerField(db_column='Code', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=50, blank=True, null=True)  # Field name made lowercase.
    comment = models.CharField(db_column='Comment', max_length=500, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RepositoryGroup'


class Rollcalltraffic(models.Model):
    trid = models.BigAutoField(db_column='TrID', primary_key=True)  # Field name made lowercase.
    cardnumber = models.BigIntegerField(db_column='CardNumber')  # Field name made lowercase.
    trdate = models.CharField(db_column='TrDate', max_length=10)  # Field name made lowercase.
    trtime = models.CharField(db_column='TrTime', max_length=5)  # Field name made lowercase.
    trtype = models.SmallIntegerField(db_column='TrType')  # Field name made lowercase.
    trday = models.SmallIntegerField(db_column='TrDay', blank=True, null=True)  # Field name made lowercase.
    isdevice = models.BooleanField(db_column='IsDevice')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RollCallTraffic'


class Smsdatabase(models.Model):
    title = models.CharField(db_column='Title', max_length=50, blank=True, null=True)  # Field name made lowercase.
    servername = models.CharField(db_column='ServerName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    databasename = models.CharField(db_column='DatabaseName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    userid = models.CharField(db_column='UserId', max_length=50, blank=True, null=True)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=50, blank=True, null=True)  # Field name made lowercase.
    winauthe = models.BooleanField(db_column='WinAuthe', blank=True, null=True)  # Field name made lowercase.
    query = models.CharField(db_column='Query', max_length=500, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SMSDataBase'


class Smsonlineservice(models.Model):
    id = models.IntegerField(db_column='ID', blank=True, primary_key=True)  # Field name made lowercase.
    serviceonlineid = models.IntegerField(db_column='ServiceOnlineID', blank=True, null=True)  # Field name made lowercase.
    aidserviceid = models.IntegerField(db_column='AIDServiceID', blank=True, null=True)  # Field name made lowercase.
    typeservice = models.IntegerField(db_column='TypeService', blank=True, null=True)  # Field name made lowercase.
    idtype = models.IntegerField(db_column='IDType', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SMSOnlineService'


class SmsoperationSend(models.Model):
    message = models.CharField(db_column='Message', max_length=500, blank=True, null=True)  # Field name made lowercase.
    mobilenum = models.CharField(db_column='MobileNum', max_length=20, blank=True, null=True)  # Field name made lowercase.
    sentbit = models.BooleanField(db_column='SentBit', blank=True, null=True)  # Field name made lowercase.
    type = models.SmallIntegerField(db_column='Type', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SMSOperation_send'


class Smsscheduling(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    scheduletitle = models.CharField(db_column='ScheduleTitle', max_length=50)  # Field name made lowercase.
    scheduledate = models.CharField(db_column='ScheduleDate', max_length=10)  # Field name made lowercase.
    stime = models.CharField(db_column='STime', max_length=5)  # Field name made lowercase.
    etime = models.CharField(db_column='ETime', max_length=5)  # Field name made lowercase.
    smstext = models.CharField(db_column='SMSText', max_length=500)  # Field name made lowercase.
    mobilenumlist = models.CharField(db_column='MobileNumList', max_length=6000, blank=True, null=True)  # Field name made lowercase.
    filterstring = models.CharField(db_column='FilterString', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    filterpersian = models.CharField(db_column='FilterPersian', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    schedulecomment = models.CharField(db_column='ScheduleComment', max_length=500, blank=True, null=True)  # Field name made lowercase.
    done = models.BooleanField(db_column='Done', blank=True, null=True)  # Field name made lowercase.
    onlineservice = models.BooleanField(db_column='OnlineService')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SMSScheduling'


class Salarybill(models.Model):
    code = models.IntegerField(db_column='Code', primary_key=True)  # Field name made lowercase.
    matter = models.CharField(db_column='Matter', max_length=50)  # Field name made lowercase.
    staffcode = models.IntegerField(db_column='StaffCode')  # Field name made lowercase.
    comment = models.CharField(db_column='Comment', max_length=500, blank=True, null=True)  # Field name made lowercase.
    insurancein = models.DecimalField(db_column='InsuranceIn', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    taxin = models.DecimalField(db_column='TaxIn', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    output = models.IntegerField(db_column='OutPut')  # Field name made lowercase.
    fromdate = models.CharField(db_column='FromDate', max_length=10)  # Field name made lowercase.
    todate = models.CharField(db_column='ToDate', max_length=10)  # Field name made lowercase.
    vouchercode = models.IntegerField(db_column='VoucherCode', blank=True, null=True)  # Field name made lowercase.
    expcentercode = models.IntegerField(db_column='ExpCenterCode', blank=True, null=True)  # Field name made lowercase.
    createdtime = models.CharField(db_column='CreatedTime', max_length=5, blank=True, null=True)  # Field name made lowercase.
    createddate = models.CharField(db_column='CreatedDate', max_length=10, blank=True, null=True)  # Field name made lowercase.
    modifiedtime = models.CharField(db_column='ModifiedTime', max_length=5, blank=True, null=True)  # Field name made lowercase.
    modifieddate = models.CharField(db_column='ModifiedDate', max_length=10, blank=True, null=True)  # Field name made lowercase.
    usercreated = models.IntegerField(db_column='UserCreated')  # Field name made lowercase.
    usermodified = models.IntegerField(db_column='UserModified', blank=True, null=True)  # Field name made lowercase.
    owner = models.IntegerField(db_column='Owner')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SalaryBill'


class Salarybilldetail(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    salarybillcode = models.ForeignKey(Salarybill, on_delete=models.DO_NOTHING, db_column='SalaryBillCode')  # Field name made lowercase.
    itemcode = models.IntegerField(db_column='ItemCode')  # Field name made lowercase.
    amount = models.DecimalField(db_column='Amount', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    cost = models.DecimalField(db_column='Cost', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    comment = models.CharField(db_column='Comment', max_length=500, blank=True, null=True)  # Field name made lowercase.
    auto = models.BooleanField(db_column='Auto')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SalaryBillDetail'


class Sales(models.Model):
    id = models.BigIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    date = models.CharField(db_column='Date', max_length=8, blank=True, null=True)  # Field name made lowercase.
    time = models.CharField(db_column='Time', max_length=5, blank=True, null=True)  # Field name made lowercase.
    receipt = models.IntegerField(db_column='Receipt', blank=True, null=True)  # Field name made lowercase.
    scaleno = models.IntegerField(db_column='ScaleNo', blank=True, null=True)  # Field name made lowercase.
    vendorno = models.IntegerField(db_column='VendorNo', blank=True, null=True)  # Field name made lowercase.
    totalprice = models.BigIntegerField(db_column='TotalPrice', blank=True, null=True)  # Field name made lowercase.
    totaldiscountpercent = models.SmallIntegerField(db_column='TotalDisCountPercent', blank=True, null=True)  # Field name made lowercase.
    totaldiscount = models.BigIntegerField(db_column='TotalDisCount', blank=True, null=True)  # Field name made lowercase.
    finalprice = models.BigIntegerField(db_column='FinalPrice', blank=True, null=True)  # Field name made lowercase.
    itemcode = models.IntegerField(db_column='ItemCode', blank=True, null=True)  # Field name made lowercase.
    itemtype = models.CharField(db_column='ItemType', max_length=1, blank=True, null=True)  # Field name made lowercase.
    unitprice = models.IntegerField(db_column='UnitPrice', blank=True, null=True)  # Field name made lowercase.
    price = models.IntegerField(db_column='Price', blank=True, null=True)  # Field name made lowercase.
    discountpercent = models.SmallIntegerField(db_column='DiscountPercent', blank=True, null=True)  # Field name made lowercase.
    discount = models.IntegerField(db_column='Discount', blank=True, null=True)  # Field name made lowercase.
    rowfinalprice = models.IntegerField(db_column='RowFinalPrice', blank=True, null=True)  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=1, blank=True, null=True)  # Field name made lowercase.
    vat = models.IntegerField(db_column='Vat', blank=True, null=True)  # Field name made lowercase.
    receiptline = models.IntegerField(db_column='ReceiptLine', blank=True, null=True)  # Field name made lowercase.
    amount = models.CharField(db_column='Amount', max_length=6, blank=True, null=True)  # Field name made lowercase.
    vatpercent = models.CharField(db_column='VatPercent', max_length=5, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Sales'


class Salescopy(models.Model):
    id = models.BigIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    date = models.CharField(db_column='Date', max_length=8, blank=True, null=True)  # Field name made lowercase.
    time = models.CharField(db_column='Time', max_length=5, blank=True, null=True)  # Field name made lowercase.
    receipt = models.IntegerField(db_column='Receipt', blank=True, null=True)  # Field name made lowercase.
    scaleno = models.IntegerField(db_column='ScaleNo', blank=True, null=True)  # Field name made lowercase.
    vendorno = models.IntegerField(db_column='VendorNo', blank=True, null=True)  # Field name made lowercase.
    totalprice = models.BigIntegerField(db_column='TotalPrice', blank=True, null=True)  # Field name made lowercase.
    totaldiscountpercent = models.SmallIntegerField(db_column='TotalDisCountPercent', blank=True, null=True)  # Field name made lowercase.
    totaldiscount = models.BigIntegerField(db_column='TotalDisCount', blank=True, null=True)  # Field name made lowercase.
    finalprice = models.BigIntegerField(db_column='FinalPrice', blank=True, null=True)  # Field name made lowercase.
    itemcode = models.IntegerField(db_column='ItemCode', blank=True, null=True)  # Field name made lowercase.
    itemtype = models.CharField(db_column='ItemType', max_length=1, blank=True, null=True)  # Field name made lowercase.
    unitprice = models.IntegerField(db_column='UnitPrice', blank=True, null=True)  # Field name made lowercase.
    price = models.IntegerField(db_column='Price', blank=True, null=True)  # Field name made lowercase.
    discountpercent = models.SmallIntegerField(db_column='DiscountPercent', blank=True, null=True)  # Field name made lowercase.
    discount = models.IntegerField(db_column='Discount', blank=True, null=True)  # Field name made lowercase.
    rowfinalprice = models.IntegerField(db_column='RowFinalPrice', blank=True, null=True)  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=1, blank=True, null=True)  # Field name made lowercase.
    vat = models.IntegerField(db_column='Vat', blank=True, null=True)  # Field name made lowercase.
    receiptline = models.IntegerField(db_column='ReceiptLine', blank=True, null=True)  # Field name made lowercase.
    amount = models.CharField(db_column='Amount', max_length=6, blank=True, null=True)  # Field name made lowercase.
    vatpercent = models.CharField(db_column='VatPercent', max_length=5, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SalesCopy'


class Salesview(models.Model):
    id = models.BigIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    date = models.CharField(db_column='Date', max_length=8, blank=True, null=True)  # Field name made lowercase.
    time = models.CharField(db_column='Time', max_length=5, blank=True, null=True)  # Field name made lowercase.
    receipt = models.IntegerField(db_column='Receipt', blank=True, null=True)  # Field name made lowercase.
    scaleno = models.IntegerField(db_column='ScaleNo', blank=True, null=True)  # Field name made lowercase.
    vendorno = models.IntegerField(db_column='VendorNo', blank=True, null=True)  # Field name made lowercase.
    totalprice = models.BigIntegerField(db_column='TotalPrice', blank=True, null=True)  # Field name made lowercase.
    totaldiscountpercent = models.SmallIntegerField(db_column='TotalDisCountPercent', blank=True, null=True)  # Field name made lowercase.
    totaldiscount = models.BigIntegerField(db_column='TotalDisCount', blank=True, null=True)  # Field name made lowercase.
    finalprice = models.BigIntegerField(db_column='FinalPrice', blank=True, null=True)  # Field name made lowercase.
    itemcode = models.IntegerField(db_column='ItemCode', blank=True, null=True)  # Field name made lowercase.
    itemtype = models.CharField(db_column='ItemType', max_length=1, blank=True, null=True)  # Field name made lowercase.
    unitprice = models.IntegerField(db_column='UnitPrice', blank=True, null=True)  # Field name made lowercase.
    price = models.IntegerField(db_column='Price', blank=True, null=True)  # Field name made lowercase.
    discountpercent = models.SmallIntegerField(db_column='DiscountPercent', blank=True, null=True)  # Field name made lowercase.
    discount = models.IntegerField(db_column='Discount', blank=True, null=True)  # Field name made lowercase.
    rowfinalprice = models.IntegerField(db_column='RowFinalPrice', blank=True, null=True)  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=1, blank=True, null=True)  # Field name made lowercase.
    vat = models.IntegerField(db_column='Vat', blank=True, null=True)  # Field name made lowercase.
    receiptline = models.IntegerField(db_column='ReceiptLine', blank=True, null=True)  # Field name made lowercase.
    amount = models.CharField(db_column='Amount', max_length=6, blank=True, null=True)  # Field name made lowercase.
    vatpercent = models.CharField(db_column='VatPercent', max_length=5, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Salesview'


class Sanad(models.Model):
    code = models.IntegerField()
    tarikh = models.CharField(max_length=10, blank=True, null=True)
    zamaem = models.SmallIntegerField(blank=True, null=True)
    sharh = models.CharField(max_length=500, blank=True, null=True)
    status = models.SmallIntegerField()
    com_index = models.IntegerField(db_column='Com_Index')  # Field name made lowercase.
    sanadid =  models.AutoField(db_column='SanadID',primary_key=True)  # Field name made lowercase.
    lastprintdate = models.CharField(db_column='LastPrintDate', max_length=10, blank=True, null=True)  # Field name made lowercase.
    usercode = models.IntegerField(db_column='UserCode', blank=True, null=True)  # Field name made lowercase.
    createdtime = models.CharField(db_column='CreatedTime', max_length=5, blank=True, null=True)  # Field name made lowercase.
    createddate = models.CharField(db_column='CreatedDate', max_length=10, blank=True, null=True)  # Field name made lowercase.
    modifiedtime = models.CharField(db_column='ModifiedTime', max_length=5, blank=True, null=True)  # Field name made lowercase.
    modifieddate = models.CharField(db_column='ModifiedDate', max_length=10, blank=True, null=True)  # Field name made lowercase.
    usercreated = models.CharField(db_column='UserCreated', max_length=50, blank=True, null=True)  # Field name made lowercase.
    usermodified = models.CharField(db_column='UserModified', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Sanad'


class Sanadprint1(models.Model):
    sanadcode = models.IntegerField(db_column='SanadCode')  # Field name made lowercase.
    kol = models.CharField(db_column='Kol', max_length=5, blank=True, null=True)  # Field name made lowercase.
    moin = models.CharField(db_column='Moin', max_length=5, blank=True, null=True)  # Field name made lowercase.
    tafsili = models.CharField(db_column='Tafsili', max_length=8, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=200, blank=True, null=True)  # Field name made lowercase.
    comment = models.CharField(db_column='Comment', max_length=500, blank=True, null=True)  # Field name made lowercase.
    costmoin = models.DecimalField(db_column='CostMoin', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    costtafsili = models.DecimalField(db_column='CostTafsili', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    bed = models.DecimalField(db_column='Bed', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    bes = models.DecimalField(db_column='Bes', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    type = models.BigIntegerField(db_column='Type', blank=True, null=True)  # Field name made lowercase.
    type2 = models.BooleanField(db_column='Type2', blank=True, null=True)  # Field name made lowercase.
    amount = models.IntegerField(db_column='Amount', blank=True, null=True)  # Field name made lowercase.
    untname = models.CharField(db_column='untName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    tafsili2 = models.CharField(db_column='Tafsili2', max_length=5, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SanadPrint1'


class SanadCheque(models.Model):
    id = id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    sanad_code = models.IntegerField(db_column='Sanad_Code', blank=True, null=True)  # Field name made lowercase.
    chequerow = models.IntegerField(db_column='ChequeRow', blank=True, null=True)  # Field name made lowercase.
    accountrow = models.IntegerField(db_column='AccountRow', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Sanad_Cheque'


class SanadChequeTmp(models.Model):
    id = id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    sanad_code = models.IntegerField(db_column='Sanad_Code', blank=True, null=True)  # Field name made lowercase.
    chequerow = models.IntegerField(db_column='ChequeRow', blank=True, null=True)  # Field name made lowercase.
    accountrow = models.IntegerField(db_column='AccountRow', blank=True, null=True)  # Field name made lowercase.
    isopen = models.BooleanField(db_column='IsOpen', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Sanad_Cheque_tmp'


class SanadDetail(models.Model):
    # فیلد اصلی برای Django - کلید خارجی به Sanad
    sanad = models.ForeignKey('Sanad', on_delete=models.CASCADE, db_column='code')
    radif = models.IntegerField()
    kol = models.SmallIntegerField(blank=True, null=True)
    moin = models.SmallIntegerField(blank=True, null=True)
    tafzili = models.IntegerField(blank=True, null=True)
    sharh = models.CharField(max_length=500, blank=True, null=True)
    status = models.SmallIntegerField(blank=True, null=True)
    bed = models.DecimalField(max_digits=23, decimal_places=9, blank=True, null=True)
    bes = models.DecimalField(max_digits=23, decimal_places=9, blank=True, null=True)
    sanad_code = models.CharField(db_column='Sanad_Code', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sanad_type = models.IntegerField(db_column='Sanad_Type', blank=True, null=True)  # Field name made lowercase.
    meghdar = models.DecimalField(db_column='Meghdar', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    com_index = models.IntegerField(db_column='Com_Index')  # Field name made lowercase.
    zamaem = models.IntegerField(db_column='Zamaem', blank=True, null=True)  # Field name made lowercase.
    store = models.SmallIntegerField(db_column='Store', blank=True, null=True)  # Field name made lowercase.
    tafsili2 = models.IntegerField(db_column='Tafsili2', blank=True, null=True)  # Field name made lowercase.
    voucherdate = models.CharField(db_column='VoucherDate', max_length=10, blank=True, null=True)  # Field name made lowercase.
    operationdate = models.CharField(db_column='OperationDate', max_length=10, blank=True, null=True)  # Field name made lowercase.
    syscomment = models.CharField(db_column='SysComment', max_length=1100, blank=True, null=True)  # Field name made lowercase.
    currcode = models.IntegerField(db_column='CurrCode', blank=True, null=True)  # Field name made lowercase.
    curramount = models.DecimalField(db_column='CurrAmount', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    currrate = models.DecimalField(db_column='CurrRate', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    usercode = models.IntegerField(db_column='UserCode', blank=True, null=True)  # Field name made lowercase.
    global_field = models.ForeignKey(GlobalIds, on_delete=models.DO_NOTHING, db_column='Global_ID', blank=True, null=True)  # Field name made lowercase. Field renamed because it was a Python reserved word.
    createdtime = models.CharField(db_column='CreatedTime', max_length=5, blank=True, null=True)  # Field name made lowercase.
    createddate = models.CharField(db_column='CreatedDate', max_length=10, blank=True, null=True)  # Field name made lowercase.
    modifiedtime = models.CharField(db_column='ModifiedTime', max_length=5, blank=True, null=True)  # Field name made lowercase.
    modifieddate = models.CharField(db_column='ModifiedDate', max_length=10, blank=True, null=True)  # Field name made lowercase.
    usercreated = models.CharField(db_column='UserCreated', max_length=50, blank=True, null=True)  # Field name made lowercase.
    usermodified = models.CharField(db_column='UserModified', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Sanad_detail'
        unique_together = (('sanad', 'radif'),)


class SandoghTbl(models.Model):
    code = models.IntegerField(db_column='Code', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=50, blank=True, null=True)  # Field name made lowercase.
    comment = models.CharField(db_column='Comment', max_length=500, blank=True, null=True)  # Field name made lowercase.
    mogodi = models.DecimalField(db_column='Mogodi', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    avaldore = models.DecimalField(db_column='AvalDore', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    vouchercode = models.IntegerField(db_column='VoucherCode', blank=True, null=True)  # Field name made lowercase.
    currcode = models.IntegerField(db_column='CurrCode', blank=True, null=True)  # Field name made lowercase.
    currrate = models.DecimalField(db_column='CurrRate', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    createdtime = models.CharField(db_column='CreatedTime', max_length=5, blank=True, null=True)  # Field name made lowercase.
    createddate = models.CharField(db_column='CreatedDate', max_length=10, blank=True, null=True)  # Field name made lowercase.
    modifiedtime = models.CharField(db_column='ModifiedTime', max_length=5, blank=True, null=True)  # Field name made lowercase.
    modifieddate = models.CharField(db_column='ModifiedDate', max_length=10, blank=True, null=True)  # Field name made lowercase.
    usercreated = models.CharField(db_column='UserCreated', max_length=50, blank=True, null=True)  # Field name made lowercase.
    usermodified = models.CharField(db_column='UserModified', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Sandogh_TBL'


class Saveruin(models.Model):
    code = models.IntegerField(db_column='Code', primary_key=True)  # Field name made lowercase.
    obtaincode = models.ForeignKey(Obtain, on_delete=models.DO_NOTHING, db_column='ObtainCode', related_name='ruin_records')   
    date = models.CharField(db_column='Date', max_length=10)  # Field name made lowercase.
    ruinmethod = models.IntegerField(db_column='RuinMethod', blank=True, null=True)  # Field name made lowercase.
    amount = models.DecimalField(db_column='Amount', max_digits=23, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    cost = models.DecimalField(db_column='Cost', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    comment = models.CharField(db_column='Comment', max_length=500, blank=True, null=True)  # Field name made lowercase.
    vouchercode = models.IntegerField(db_column='VoucherCode', blank=True, null=True)  # Field name made lowercase.
    expcentercode = models.IntegerField(db_column='ExpCenterCode', blank=True, null=True)  # Field name made lowercase.
    createdtime = models.CharField(db_column='CreatedTime', max_length=5)  # Field name made lowercase.
    createddate = models.CharField(db_column='CreatedDate', max_length=10)  # Field name made lowercase.
    usercreated = models.IntegerField(db_column='UserCreated')  # Field name made lowercase.
    modifiedtime = models.CharField(db_column='ModifiedTime', max_length=5, blank=True, null=True)  # Field name made lowercase.
    modifieddate = models.CharField(db_column='ModifiedDate', max_length=10, blank=True, null=True)  # Field name made lowercase.
    usermodified = models.IntegerField(db_column='UserModified', blank=True, null=True)  # Field name made lowercase.
    owner = models.IntegerField(db_column='Owner')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SaveRuin'


class Scalebarcodeformul(models.Model):
    scalebarcodeid = models.IntegerField(db_column='ScaleBarCodeID', primary_key=True)  # Field name made lowercase.
    barcodetitle = models.CharField(db_column='BarCodeTitle', max_length=100)  # Field name made lowercase.
    barcodetype = models.SmallIntegerField(db_column='BarCodeType')  # Field name made lowercase.
    digitcount = models.SmallIntegerField(db_column='DigitCount')  # Field name made lowercase.
    constantstart = models.SmallIntegerField(db_column='ConstantStart', blank=True, null=True)  # Field name made lowercase.
    constantcount = models.IntegerField(db_column='ConstantCount', blank=True, null=True)  # Field name made lowercase.
    constantcode = models.CharField(db_column='ConstantCode', max_length=10, blank=True, null=True)  # Field name made lowercase.
    scalenumberstart = models.SmallIntegerField(db_column='ScaleNumberStart', blank=True, null=True)  # Field name made lowercase.
    scalenumbercount = models.SmallIntegerField(db_column='ScaleNumberCount', blank=True, null=True)  # Field name made lowercase.
    memoryfactnumberstart = models.SmallIntegerField(db_column='MemoryFactNumberStart', blank=True, null=True)  # Field name made lowercase.
    memoryfactnumbercount = models.SmallIntegerField(db_column='MemoryFactNumberCount', blank=True, null=True)  # Field name made lowercase.
    factornumberstart = models.SmallIntegerField(db_column='FactorNumberStart', blank=True, null=True)  # Field name made lowercase.
    factornumbercount = models.SmallIntegerField(db_column='FactorNumberCount', blank=True, null=True)  # Field name made lowercase.
    factordatestart = models.SmallIntegerField(db_column='FactorDateStart', blank=True, null=True)  # Field name made lowercase.
    factordatecount = models.SmallIntegerField(db_column='FactorDateCount', blank=True, null=True)  # Field name made lowercase.
    rowcounterstart = models.SmallIntegerField(db_column='RowCounterStart', blank=True, null=True)  # Field name made lowercase.
    rowcountercount = models.SmallIntegerField(db_column='RowCounterCount', blank=True, null=True)  # Field name made lowercase.
    sumpricestart = models.SmallIntegerField(db_column='SumPriceStart', blank=True, null=True)  # Field name made lowercase.
    sumpricecount = models.SmallIntegerField(db_column='SumPriceCount', blank=True, null=True)  # Field name made lowercase.
    unuseddigitcount = models.SmallIntegerField(db_column='UnUsedDigitCount', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ScaleBarCodeFormul'


class Scalefactor(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    cashier = models.CharField(db_column='Cashier', max_length=10, blank=True, null=True)  # Field name made lowercase.
    factordate = models.CharField(db_column='FactorDate', max_length=10, blank=True, null=True)  # Field name made lowercase.
    factortime = models.CharField(db_column='FactorTime', max_length=10, blank=True, null=True)  # Field name made lowercase.
    memorynumber = models.IntegerField(db_column='MemoryNumber', blank=True, null=True)  # Field name made lowercase.
    factornumber = models.IntegerField(db_column='FactorNumber', blank=True, null=True)  # Field name made lowercase.
    offpercent = models.DecimalField(db_column='OffPercent', max_digits=23, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    productcount = models.IntegerField(db_column='ProductCount', blank=True, null=True)  # Field name made lowercase.
    scalename = models.CharField(db_column='ScaleName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sumall = models.DecimalField(db_column='SumAll', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    sumtotal = models.DecimalField(db_column='SumTotal', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    tax = models.DecimalField(db_column='Tax', max_digits=23, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    scale = models.IntegerField(db_column='Scale', blank=True, null=True)  # Field name made lowercase.
    savefactor = models.BooleanField(db_column='SaveFactor', blank=True, null=True)  # Field name made lowercase.
    scaleid = models.IntegerField(db_column='ScaleID', blank=True, null=True)  # Field name made lowercase.
    servicerowversion = models.BigIntegerField(db_column='ServiceRowVersion')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ScaleFactor'


class Scalefactoritems(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    factornumber = models.IntegerField(db_column='FactorNumber', blank=True, null=True)  # Field name made lowercase.
    factordate = models.CharField(db_column='FactorDate', max_length=10, blank=True, null=True)  # Field name made lowercase.
    itemcount = models.IntegerField(db_column='ItemCount', blank=True, null=True)  # Field name made lowercase.
    memorynumberitem = models.IntegerField(db_column='MemoryNumberItem', blank=True, null=True)  # Field name made lowercase.
    price = models.DecimalField(db_column='Price', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    productcode = models.IntegerField(db_column='ProductCode', blank=True, null=True)  # Field name made lowercase.
    unitprice = models.DecimalField(db_column='UnitPrice', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    weightorcount = models.DecimalField(db_column='WeightOrCount', max_digits=23, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    scale = models.IntegerField(db_column='Scale', blank=True, null=True)  # Field name made lowercase.
    factorid = models.ForeignKey(Scalefactor, on_delete=models.DO_NOTHING, db_column='FactorID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ScaleFactorItems'


class Scalevendor(models.Model):
    scale = models.IntegerField(db_column='Scale', primary_key=True)  # Field name made lowercase.
    vendor1 = models.IntegerField(db_column='Vendor1', blank=True, null=True)  # Field name made lowercase.
    vendor2 = models.IntegerField(db_column='Vendor2', blank=True, null=True)  # Field name made lowercase.
    vendor3 = models.IntegerField(db_column='Vendor3', blank=True, null=True)  # Field name made lowercase.
    vendor4 = models.IntegerField(db_column='Vendor4', blank=True, null=True)  # Field name made lowercase.
    vendor5 = models.IntegerField(db_column='Vendor5', blank=True, null=True)  # Field name made lowercase.
    vendor6 = models.IntegerField(db_column='Vendor6', blank=True, null=True)  # Field name made lowercase.
    vendor7 = models.IntegerField(db_column='Vendor7', blank=True, null=True)  # Field name made lowercase.
    vendor8 = models.IntegerField(db_column='Vendor8', blank=True, null=True)  # Field name made lowercase.
    vendor9 = models.IntegerField(db_column='Vendor9', blank=True, null=True)  # Field name made lowercase.
    vendor10 = models.IntegerField(db_column='Vendor10', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ScaleVendor'


class Scales(models.Model):
    ip = models.IntegerField(db_column='IP', primary_key=True)  # Field name made lowercase.
    number = models.CharField(db_column='Number', max_length=2, blank=True, null=True)  # Field name made lowercase.
    date = models.DateTimeField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
    zreport = models.BooleanField(db_column='ZReport', blank=True, null=True)  # Field name made lowercase.
    iprange = models.CharField(db_column='ipRange', max_length=15, blank=True, null=True)  # Field name made lowercase.
    scaleport = models.IntegerField(db_column='ScalePort', blank=True, null=True)  # Field name made lowercase.
    serveriprange = models.CharField(db_column='ServerIpRange', max_length=15, blank=True, null=True)  # Field name made lowercase.
    portrx = models.IntegerField(db_column='PortRx', blank=True, null=True)  # Field name made lowercase.
    porttx = models.IntegerField(db_column='PortTx', blank=True, null=True)  # Field name made lowercase.
    scalemodel = models.CharField(db_column='ScaleModel', max_length=50, blank=True, null=True)  # Field name made lowercase.
    scaletype = models.SmallIntegerField(db_column='ScaleType', blank=True, null=True)  # Field name made lowercase.
    isactive = models.BooleanField(db_column='isActive')  # Field name made lowercase.
    connecttype = models.SmallIntegerField(db_column='ConnectType')  # Field name made lowercase.
    divto = models.SmallIntegerField(db_column='DivTo')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Scales'


class ScalesGroups(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    groupno = models.IntegerField(db_column='GroupNo', blank=True, null=True)  # Field name made lowercase.
    scalecode = models.IntegerField(db_column='ScaleCode', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Scales_Groups'


class Secondaryaccount(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    shareholdercode = models.ForeignKey('Shareholder', on_delete=models.DO_NOTHING, db_column='ShareHolderCode')  # Field name made lowercase.
    percode = models.IntegerField(db_column='PerCode')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SecondaryAccount'


class SelectedlistDetail(models.Model):
    sl_code = models.ForeignKey('Selectedlists', on_delete=models.DO_NOTHING, db_column='SL_Code')  # Field name made lowercase.
    code = models.IntegerField(db_column='Code')  # Field name made lowercase.
    radif = models.IntegerField(db_column='Radif', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SelectedList_Detail'


class Selectedlists(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    code = models.IntegerField(db_column='Code')  # Field name made lowercase.
    type = models.SmallIntegerField(db_column='Type')  # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=100)  # Field name made lowercase.
    comment = models.CharField(db_column='Comment', max_length=500, blank=True, null=True)  # Field name made lowercase.
    enable = models.BooleanField(db_column='Enable')  # Field name made lowercase.
    displaytype = models.IntegerField(db_column='DisplayType', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SelectedLists'


class Sellqueue(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    ordercode = models.ForeignKey(Order, on_delete=models.DO_NOTHING, db_column='OrderCode')  # Field name made lowercase.
    enterdate = models.CharField(db_column='EnterDate', max_length=10)  # Field name made lowercase.
    entertime = models.CharField(db_column='EnterTime', max_length=5)  # Field name made lowercase.
    factcode = models.IntegerField(db_column='FactCode', blank=True, null=True)  # Field name made lowercase.
    exittime = models.CharField(db_column='ExitTime', max_length=5, blank=True, null=True)  # Field name made lowercase.
    userid = models.ForeignKey('Users', on_delete=models.DO_NOTHING, db_column='UserId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SellQueue'


class Sellreports(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    reporttype = models.SmallIntegerField(db_column='ReportType', blank=True, null=True)  # Field name made lowercase.
    reportspname = models.CharField(db_column='ReportSpName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    reporttitle = models.CharField(db_column='ReportTitle', max_length=500, blank=True, null=True)  # Field name made lowercase.
    reportgroup = models.SmallIntegerField(db_column='ReportGroup', blank=True, null=True)  # Field name made lowercase.
    base1 = models.IntegerField(db_column='Base1', blank=True, null=True)  # Field name made lowercase.
    base2 = models.IntegerField(db_column='Base2', blank=True, null=True)  # Field name made lowercase.
    base3 = models.IntegerField(db_column='Base3', blank=True, null=True)  # Field name made lowercase.
    timerangetype = models.SmallIntegerField(db_column='TimeRangeType', blank=True, null=True)  # Field name made lowercase.
    timerangefromdate = models.CharField(db_column='TimeRangeFromDate', max_length=10, blank=True, null=True)  # Field name made lowercase.
    timerangetodate = models.CharField(db_column='TimeRangeToDate', max_length=10, blank=True, null=True)  # Field name made lowercase.
    grouppersoncode = models.IntegerField(db_column='GroupPersonCode', blank=True, null=True)  # Field name made lowercase.
    personselectedlistcode = models.IntegerField(db_column='PersonSelectedListCode', blank=True, null=True)  # Field name made lowercase.
    personselectedlist = models.BooleanField(db_column='PersonSelectedList', blank=True, null=True)  # Field name made lowercase.
    personlabelcode = models.CharField(db_column='PersonLabelCode', max_length=50, blank=True, null=True)  # Field name made lowercase.
    personcategorycode = models.IntegerField(db_column='PersonCategoryCode', blank=True, null=True)  # Field name made lowercase.
    groupdaramadcode = models.IntegerField(db_column='GroupDaramadCode', blank=True, null=True)  # Field name made lowercase.
    goodgroupcode = models.IntegerField(db_column='GoodGroupCode', blank=True, null=True)  # Field name made lowercase.
    goodselectedlistcode = models.IntegerField(db_column='GoodSelectedListCode', blank=True, null=True)  # Field name made lowercase.
    goodselectedlist = models.BooleanField(db_column='GoodSelectedList', blank=True, null=True)  # Field name made lowercase.
    goodlabelcode = models.CharField(db_column='GoodLabelCode', max_length=50, blank=True, null=True)  # Field name made lowercase.
    goodcategorycode = models.IntegerField(db_column='GoodCategoryCode', blank=True, null=True)  # Field name made lowercase.
    sortorder1code = models.IntegerField(db_column='SortOrder1Code', blank=True, null=True)  # Field name made lowercase.
    sortorder1type = models.SmallIntegerField(db_column='SortOrder1Type', blank=True, null=True)  # Field name made lowercase.
    sortorder2code = models.IntegerField(db_column='SortOrder2Code', blank=True, null=True)  # Field name made lowercase.
    sortorder2type = models.SmallIntegerField(db_column='SortOrder2Type', blank=True, null=True)  # Field name made lowercase.
    sortorder3code = models.IntegerField(db_column='SortOrder3Code', blank=True, null=True)  # Field name made lowercase.
    sortorder3type = models.SmallIntegerField(db_column='SortOrder3Type', blank=True, null=True)  # Field name made lowercase.
    selecttoprecordvalue = models.IntegerField(db_column='SelectTopRecordValue', blank=True, null=True)  # Field name made lowercase.
    createdtime = models.CharField(db_column='CreatedTime', max_length=5, blank=True, null=True)  # Field name made lowercase.
    createddate = models.CharField(db_column='CreatedDate', max_length=10, blank=True, null=True)  # Field name made lowercase.
    modifiedtime = models.CharField(db_column='ModifiedTime', max_length=5, blank=True, null=True)  # Field name made lowercase.
    modifieddate = models.CharField(db_column='ModifiedDate', max_length=10, blank=True, null=True)  # Field name made lowercase.
    usercreated = models.CharField(db_column='UserCreated', max_length=50, blank=True, null=True)  # Field name made lowercase.
    usermodified = models.CharField(db_column='UserModified', max_length=50, blank=True, null=True)  # Field name made lowercase.
    datestatus = models.IntegerField(db_column='DateStatus', blank=True, null=True)  # Field name made lowercase.
    generalfactorcodetype = models.IntegerField(db_column='GeneralFactorCodeType', blank=True, null=True)  # Field name made lowercase.
    generalfactorcode = models.IntegerField(db_column='GeneralFactorCode', blank=True, null=True)  # Field name made lowercase.
    generalfactorcoderangetype = models.IntegerField(db_column='GeneralFactorCodeRangeType', blank=True, null=True)  # Field name made lowercase.
    generalfactorfromcode = models.IntegerField(db_column='GeneralFactorFromCode', blank=True, null=True)  # Field name made lowercase.
    generalfactortocode = models.IntegerField(db_column='GeneralFactorToCode', blank=True, null=True)  # Field name made lowercase.
    detailfactorcodetype = models.IntegerField(db_column='DetailFactorCodeType', blank=True, null=True)  # Field name made lowercase.
    detailfactorcode = models.IntegerField(db_column='DetailFactorCode', blank=True, null=True)  # Field name made lowercase.
    detailfactorcoderangetype = models.IntegerField(db_column='DetailFactorCodeRangeType', blank=True, null=True)  # Field name made lowercase.
    detailfactorfromcode = models.IntegerField(db_column='DetailFactorFromCode', blank=True, null=True)  # Field name made lowercase.
    detailfactortocode = models.IntegerField(db_column='DetailFactorToCode', blank=True, null=True)  # Field name made lowercase.
    generalfactorcostrangetype = models.IntegerField(db_column='GeneralFactorCostRangeType', blank=True, null=True)  # Field name made lowercase.
    generalfactorfromcost = models.DecimalField(db_column='GeneralFactorFromCost', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    generalfactortocost = models.DecimalField(db_column='GeneralFactorToCost', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SellReports'


class Sellreportsamounts(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    sellreportsid = models.IntegerField(db_column='SellReportsID', blank=True, null=True)  # Field name made lowercase.
    sellreportsamountsid = models.IntegerField(db_column='SellReportsAmountsID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SellReportsAmounts'


class Sellreportsamountsdef(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    amountstype = models.IntegerField(db_column='AmountsType', blank=True, null=True)  # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=100, blank=True, null=True)  # Field name made lowercase.
    fieldvalue = models.CharField(db_column='FieldValue', max_length=250, blank=True, null=True)  # Field name made lowercase.
    tablename = models.CharField(db_column='TableName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    isshow = models.BooleanField(db_column='IsShow', blank=True, null=True)  # Field name made lowercase.
    footershow = models.BooleanField(db_column='FooterShow', blank=True, null=True)  # Field name made lowercase.
    footertype = models.SmallIntegerField(db_column='FooterType', blank=True, null=True)  # Field name made lowercase.
    footervalue = models.CharField(db_column='FooterValue', max_length=100, blank=True, null=True)  # Field name made lowercase.
    fielddatatype = models.IntegerField(db_column='FieldDataType', blank=True, null=True)  # Field name made lowercase.
    fieldalias = models.CharField(db_column='FieldAlias', max_length=150, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SellReportsAmountsDef'


class Sellreportsbase(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    sellreportsid = models.IntegerField(db_column='SellReportsID', blank=True, null=True)  # Field name made lowercase.
    sellreportsbasetype = models.IntegerField(db_column='SellReportsBaseType', blank=True, null=True)  # Field name made lowercase.
    sellreportsbaseid = models.IntegerField(db_column='SellReportsBaseID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SellReportsBase'


class Sellreportsbasedef(models.Model):
    code = models.IntegerField(db_column='Code', primary_key=True)  # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=100, blank=True, null=True)  # Field name made lowercase.
    amounttablename = models.CharField(db_column='AmountTableName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    amounttablefieldvalue = models.CharField(db_column='AmountTableFieldValue', max_length=500, blank=True, null=True)  # Field name made lowercase.
    amounttablefieldname = models.CharField(db_column='AmountTableFieldName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    fieldtype = models.SmallIntegerField(db_column='FieldType', blank=True, null=True)  # Field name made lowercase.
    basetablename = models.CharField(db_column='BaseTableName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    basetablekeyfield = models.CharField(db_column='BaseTableKeyField', max_length=500, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SellReportsBaseDef'


class Sellreportsbasedeffields(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    basedefaultid = models.IntegerField(db_column='BaseDefaultID', blank=True, null=True)  # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=100, blank=True, null=True)  # Field name made lowercase.
    fieldname = models.CharField(db_column='FieldName', max_length=450, blank=True, null=True)  # Field name made lowercase.
    isshow = models.BooleanField(db_column='IsShow', blank=True, null=True)  # Field name made lowercase.
    fielddatatype = models.IntegerField(db_column='FieldDataType', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SellReportsBaseDefFields'


class Sellreportsothersfields(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    sellreportsid = models.IntegerField(db_column='SellReportsID', blank=True, null=True)  # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=100, blank=True, null=True)  # Field name made lowercase.
    fieldname = models.CharField(db_column='FieldName', max_length=150, blank=True, null=True)  # Field name made lowercase.
    footershow = models.BooleanField(db_column='FooterShow', blank=True, null=True)  # Field name made lowercase.
    footertype = models.SmallIntegerField(db_column='FooterType', blank=True, null=True)  # Field name made lowercase.
    footervalue = models.CharField(db_column='FooterValue', max_length=100, blank=True, null=True)  # Field name made lowercase.
    isshow = models.BooleanField(db_column='IsShow', blank=True, null=True)  # Field name made lowercase.
    fieldtype = models.IntegerField(db_column='FieldType', blank=True, null=True)  # Field name made lowercase.
    fielddatatype = models.IntegerField(db_column='FieldDataType', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SellReportsOthersFields'


class Sellreportsusers(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    sellreportsid = models.IntegerField(db_column='SellReportsID', blank=True, null=True)  # Field name made lowercase.
    notaccessuserid = models.IntegerField(db_column='NotAccessUserID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SellReportsUsers'


class SellReportComplete(models.Model):
    factcode = models.IntegerField(db_column='FactCode', blank=True, null=True)  # Field name made lowercase.
    factdate = models.CharField(db_column='FactDate', max_length=10, blank=True, null=True)  # Field name made lowercase.
    tavasot = models.CharField(db_column='Tavasot', max_length=50, blank=True, null=True)  # Field name made lowercase.
    recieved = models.DecimalField(db_column='Recieved', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    remain = models.DecimalField(db_column='Remain', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    gi_name = models.CharField(db_column='GI_Name', max_length=153, blank=True, null=True)  # Field name made lowercase.
    unit_name = models.CharField(db_column='Unit_Name', max_length=50, blank=True, null=True)  # Field name made lowercase.
    unit2_name = models.CharField(db_column='Unit2_Name', max_length=50, blank=True, null=True)  # Field name made lowercase.
    gi_code = models.IntegerField(db_column='GI_Code', blank=True, null=True)  # Field name made lowercase.
    amount = models.DecimalField(db_column='Amount', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    amount2 = models.DecimalField(db_column='Amount2', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    totalamount = models.IntegerField(db_column='TotalAmount', blank=True, null=True)  # Field name made lowercase.
    cost = models.DecimalField(db_column='Cost', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    totalcost = models.DecimalField(db_column='TotalCost', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    discount = models.DecimalField(db_column='Discount', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    realcost = models.DecimalField(db_column='RealCost', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    percode = models.IntegerField(db_column='PerCode', blank=True, null=True)  # Field name made lowercase.
    pername = models.CharField(db_column='PerName', max_length=171, blank=True, null=True)  # Field name made lowercase.
    viscode = models.IntegerField(db_column='VisCode', blank=True, null=True)  # Field name made lowercase.
    visname = models.CharField(db_column='VisName', max_length=171, blank=True, null=True)  # Field name made lowercase.
    com_index = models.IntegerField(db_column='Com_Index', blank=True, null=True)  # Field name made lowercase.
    rowtype = models.SmallIntegerField(db_column='RowType')  # Field name made lowercase.
    group_code = models.IntegerField(db_column='Group_Code', blank=True, null=True)  # Field name made lowercase.
    group_name = models.CharField(db_column='Group_Name', max_length=50, blank=True, null=True)  # Field name made lowercase.
    chargetax = models.DecimalField(db_column='ChargeTax', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    expensecentercode = models.IntegerField(db_column='ExpenseCenterCode', blank=True, null=True)  # Field name made lowercase.
    expensecentertitle = models.CharField(db_column='ExpenseCenterTitle', max_length=100, blank=True, null=True)  # Field name made lowercase.
    backamount = models.DecimalField(db_column='BackAmount', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    backamount2 = models.DecimalField(db_column='BackAmount2', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    backtotalcost = models.DecimalField(db_column='BackTotalCost', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    backchargetax = models.DecimalField(db_column='BackChargeTax', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    backfinalcost = models.DecimalField(db_column='BackFinalCost', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    categorykalacode = models.CharField(db_column='categorykalaCode', max_length=50, blank=True, null=True)  # Field name made lowercase.
    categorypersoncode = models.CharField(db_column='categoryPersonCode', max_length=50, blank=True, null=True)  # Field name made lowercase.
    tahviltitle = models.CharField(db_column='TahvilTitle', max_length=20, blank=True, null=True)  # Field name made lowercase.
    tarikhtahvil = models.CharField(db_column='TarikhTahvil', max_length=10, blank=True, null=True)  # Field name made lowercase.
    noetasviyetitle = models.CharField(db_column='NoeTasviyeTitle', max_length=10, blank=True, null=True)  # Field name made lowercase.
    tasvietitle = models.CharField(db_column='TasvieTitle', max_length=20, blank=True, null=True)  # Field name made lowercase.
    tarikhvosoul = models.CharField(db_column='TarikhVosoul', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Sell_Report_Complete'


class Serials(models.Model):
    code = models.IntegerField()
    radif = models.SmallIntegerField()
    kala = models.IntegerField()
    type = models.SmallIntegerField()
    tmp = models.SmallIntegerField()
    meghdar = models.DecimalField(max_digits=23, decimal_places=8, blank=True, null=True)
    meghdar2 = models.DecimalField(max_digits=23, decimal_places=8, blank=True, null=True)
    sharh = models.CharField(max_length=500, blank=True, null=True)
    anbar = models.SmallIntegerField()
    percode = models.IntegerField()
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    toanbarcode = models.SmallIntegerField(db_column='ToAnbarCode', blank=True, null=True)  # Field name made lowercase.
    expiredate_sr = models.CharField(db_column='ExpireDate_SR', max_length=10, blank=True, null=True)  # Field name made lowercase.
    color_sr = models.CharField(db_column='Color_SR', max_length=50, blank=True, null=True)  # Field name made lowercase.
    size_sr = models.CharField(db_column='Size_SR', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Serials'


class Settingtemplete(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=50, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=100, blank=True, null=True)  # Field name made lowercase.
    settingfile = models.BinaryField(db_column='SettingFile', blank=True, null=True)  # Field name made lowercase.
    isdefault = models.BooleanField(db_column='IsDefault', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SettingTemplete'


class Settings(models.Model):
    # کلید اصلی مجازی برای Django - این فیلد در دیتابیس وجود ندارد
    id = models.BigAutoField(primary_key=True)
    
    # استفاده از ترکیب فیلدها به عنوان کلید اصلی
    category = models.SmallIntegerField(db_column='Category')  # Field name made lowercase.
    code = models.SmallIntegerField(db_column='Code')  # Field name made lowercase.
    managetype = models.SmallIntegerField(db_column='ManageType')  # Field name made lowercase.
    usercode = models.IntegerField(db_column='UserCode')  # Field name made lowercase.
    selected = models.BooleanField(db_column='Selected')  # Field name made lowercase.
    amount = models.DecimalField(db_column='Amount', max_digits=30, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    comment = models.CharField(db_column='Comment', max_length=2000, blank=True, null=True)  # Field name made lowercase.
    tmp = models.IntegerField(blank=True, null=True)
    
    class Meta:
        managed = False
        db_table = 'Settings'
        # تعریف کلید اصلی ترکیبی
        unique_together = (('category', 'code', 'managetype', 'usercode'),)

    class Meta:
        managed = False
        db_table = 'Settings'
    
    def __str__(self):
        return f"تنظیم {self.category}-{self.code} (نوع: {self.managetype}, کاربر: {self.usercode})"
    
    @classmethod
    def get_setting(cls, category, code, managetype=0, usercode=0, default=None):
        """
        دریافت مقدار یک تنظیم خاص
        """
        try:
            setting = cls.objects.get(
                category=category,
                code=code,
                managetype=managetype,
                usercode=usercode
            )
            return setting.comment
        except cls.DoesNotExist:
            return default
    
    @classmethod
    def set_setting(cls, category, code, value, managetype=0, usercode=0):
        """
        تنظیم مقدار یک تنظیم خاص
        """
        setting, created = cls.objects.get_or_create(
            category=category,
            code=code,
            managetype=managetype,
            usercode=usercode,
            defaults={'comment': value}
        )
        if not created:
            setting.comment = value
            setting.save()
        return setting
    
    @classmethod
    def get_person_list_sorting(cls, managetype=0, usercode=0):
        """
        دریافت تنظیم مرتب‌سازی لیست اشخاص
        """
        return cls.get_setting(
            category=3,  # تنظیمات نمایش لیست‌ها
            code=1,      # تنظیمات لیست اشخاص
            managetype=managetype,
            usercode=usercode,
            default='code'  # پیش‌فرض: مرتب‌سازی بر اساس کد
        )
    
    @classmethod
    def set_person_list_sorting(cls, sorting_field, managetype=0, usercode=0):
        """
        تنظیم مرتب‌سازی لیست اشخاص
        """
        return cls.set_setting(
            category=3,
            code=1,
            value=sorting_field,
            managetype=managetype,
            usercode=usercode
        )
    
    @classmethod
    def get_sanad_list_sorting(cls, managetype=0, usercode=0):
        """
        دریافت تنظیم مرتب‌سازی لیست اسناد
        """
        return cls.get_setting(
            category=3,  # تنظیمات نمایش لیست‌ها
            code=2,      # تنظیمات لیست اسناد
            managetype=managetype,
            usercode=usercode,
            default='date'  # پیش‌فرض: مرتب‌سازی بر اساس تاریخ
        )
    
    @classmethod
    def set_sanad_list_sorting(cls, sorting_field, managetype=0, usercode=0):
        """
        تنظیم مرتب‌سازی لیست اسناد
        """
        return cls.set_setting(
            category=3,
            code=2,
            value=sorting_field,
            managetype=managetype,
            usercode=usercode
        )


class Share(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    number = models.DecimalField(db_column='Number', max_digits=23, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    type = models.BooleanField(db_column='Type')  # Field name made lowercase.
    calctype = models.BooleanField(db_column='CalcType')  # Field name made lowercase.
    saved = models.BooleanField(db_column='Saved', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Share'


class Shareholder(models.Model):
    code = models.IntegerField(db_column='Code', primary_key=True)  # Field name made lowercase.
    percode = models.ForeignKey(Perinf, on_delete=models.DO_NOTHING, db_column='PerCode')  # Field name made lowercase.
    number = models.DecimalField(db_column='Number', max_digits=23, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    benefit = models.DecimalField(db_column='Benefit', max_digits=23, decimal_places=8)  # Field name made lowercase.
    serialnumber = models.CharField(db_column='SerialNumber', max_length=50, blank=True, null=True)  # Field name made lowercase.
    regnum = models.CharField(db_column='RegNum', max_length=50, blank=True, null=True)  # Field name made lowercase.
    comment = models.CharField(db_column='Comment', max_length=500, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ShareHolder'


class Softwarepart(models.Model):
    code = models.IntegerField(db_column='Code', primary_key=True)  # Field name made lowercase.
    parentcode = models.IntegerField(db_column='ParentCode', blank=True, null=True)  # Field name made lowercase.
    title = models.CharField(db_column='Title', unique=True, max_length=50, blank=True, null=True)  # Field name made lowercase.
    englishtitle = models.CharField(db_column='EnglishTitle', unique=True, max_length=50, blank=True, null=True)  # Field name made lowercase.
    isreport = models.BooleanField(db_column='IsReport', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SoftwarePart'


class Specialevent(models.Model):
    userid = models.IntegerField(db_column='UserID', blank=True, null=True)  # Field name made lowercase.
    partpermissionid = models.IntegerField(db_column='PartPermissionID', blank=True, null=True)  # Field name made lowercase.
    success = models.BooleanField(db_column='Success', blank=True, null=True)  # Field name made lowercase.
    date = models.CharField(db_column='Date', max_length=10, blank=True, null=True)  # Field name made lowercase.
    time = models.CharField(db_column='Time', max_length=10, blank=True, null=True)  # Field name made lowercase.
    comment = models.CharField(db_column='Comment', max_length=500, blank=True, null=True)  # Field name made lowercase.
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    operationcode = models.IntegerField(db_column='operationCode', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SpecialEvent'


class Staff(models.Model):
    code = models.IntegerField(db_column='Code', primary_key=True)  # Field name made lowercase.
    staffgroup = models.ForeignKey('Staffgroup', on_delete=models.DO_NOTHING, db_column='StaffGroup')  # Field name made lowercase.
    personnelcode = models.CharField(db_column='PersonnelCode', max_length=20)  # Field name made lowercase.
    insurancenumber = models.CharField(db_column='InsuranceNumber', max_length=20)  # Field name made lowercase.
    cardnumber = models.CharField(db_column='CardNumber', max_length=20)  # Field name made lowercase.
    nationalid = models.CharField(db_column='NationalID', max_length=20)  # Field name made lowercase.
    sex = models.BooleanField(db_column='Sex')  # Field name made lowercase.
    fathername = models.CharField(db_column='FatherName', max_length=30, blank=True, null=True)  # Field name made lowercase.
    idnumber = models.CharField(db_column='IDNumber', max_length=20, blank=True, null=True)  # Field name made lowercase.
    birthdate = models.CharField(db_column='BirthDate', max_length=10, blank=True, null=True)  # Field name made lowercase.
    birthplace = models.CharField(db_column='BirthPlace', max_length=30, blank=True, null=True)  # Field name made lowercase.
    department = models.CharField(db_column='Department', max_length=50, blank=True, null=True)  # Field name made lowercase.
    degree = models.SmallIntegerField(db_column='Degree', blank=True, null=True)  # Field name made lowercase.
    major = models.CharField(db_column='Major', max_length=50, blank=True, null=True)  # Field name made lowercase.
    military = models.SmallIntegerField(db_column='Military', blank=True, null=True)  # Field name made lowercase.
    ismarried = models.BooleanField(db_column='IsMarried')  # Field name made lowercase.
    picture = models.BinaryField(db_column='Picture', blank=True, null=True)  # Field name made lowercase.
    fingerprint = models.BinaryField(db_column='FingerPrint', blank=True, null=True)  # Field name made lowercase.
    accountnumber = models.CharField(db_column='AccountNumber', max_length=50, blank=True, null=True)  # Field name made lowercase.
    banktitle = models.CharField(db_column='BankTitle', max_length=50, blank=True, null=True)  # Field name made lowercase.
    codate = models.CharField(db_column='CoDate', max_length=10, blank=True, null=True)  # Field name made lowercase.
    job = models.CharField(db_column='Job', max_length=20, blank=True, null=True)  # Field name made lowercase.
    comment = models.CharField(db_column='Comment', max_length=500, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=50, blank=True, null=True)  # Field name made lowercase.
    lastname = models.CharField(db_column='LastName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    tel1 = models.CharField(db_column='Tel1', max_length=50, blank=True, null=True)  # Field name made lowercase.
    tel2 = models.CharField(db_column='Tel2', max_length=50, blank=True, null=True)  # Field name made lowercase.
    fax = models.CharField(db_column='Fax', max_length=50, blank=True, null=True)  # Field name made lowercase.
    mob = models.CharField(db_column='Mob', max_length=50, blank=True, null=True)  # Field name made lowercase.
    add1 = models.CharField(db_column='Add1', max_length=300, blank=True, null=True)  # Field name made lowercase.
    add2 = models.CharField(db_column='Add2', max_length=300, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=50, blank=True, null=True)  # Field name made lowercase.
    leavedate = models.CharField(db_column='LeaveDate', max_length=10, blank=True, null=True)  # Field name made lowercase.
    employment = models.IntegerField(db_column='Employment', blank=True, null=True)  # Field name made lowercase.
    postcode = models.CharField(db_column='PostCode', max_length=10, blank=True, null=True)  # Field name made lowercase.
    category = models.IntegerField(db_column='Category', blank=True, null=True)  # Field name made lowercase.
    fiscalexemption = models.IntegerField(db_column='FiscalExemption', blank=True, null=True)  # Field name made lowercase.
    national = models.IntegerField(db_column='National', blank=True, null=True)  # Field name made lowercase.
    insurance = models.IntegerField(db_column='Insurance', blank=True, null=True)  # Field name made lowercase.
    issueplace = models.CharField(db_column='IssuePlace', max_length=50, blank=True, null=True)  # Field name made lowercase.
    createdtime = models.CharField(db_column='CreatedTime', max_length=5, blank=True, null=True)  # Field name made lowercase.
    createddate = models.CharField(db_column='CreatedDate', max_length=10, blank=True, null=True)  # Field name made lowercase.
    modifiedtime = models.CharField(db_column='ModifiedTime', max_length=5, blank=True, null=True)  # Field name made lowercase.
    modifieddate = models.CharField(db_column='ModifiedDate', max_length=10, blank=True, null=True)  # Field name made lowercase.
    usercreated = models.IntegerField(db_column='UserCreated')  # Field name made lowercase.
    usermodified = models.IntegerField(db_column='UserModified', blank=True, null=True)  # Field name made lowercase.
    jobcode = models.CharField(db_column='JobCode', max_length=6, blank=True, null=True)  # Field name made lowercase.
    issuedate = models.CharField(db_column='IssueDate', max_length=10, blank=True, null=True)  # Field name made lowercase.
    jobgroup = models.CharField(db_column='JobGroup', max_length=100, blank=True, null=True)  # Field name made lowercase.
    contracttype = models.IntegerField(db_column='ContractType')  # Field name made lowercase.
    insurancename = models.CharField(db_column='InsuranceName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    workplacestatus = models.IntegerField(db_column='WorkplaceStatus')  # Field name made lowercase.
    daraeistatus = models.CharField(db_column='DaraeiStatus', max_length=50)  # Field name made lowercase.
    hashdaraee = models.CharField(max_length=20, blank=True, null=True)
    banktypecode = models.IntegerField(db_column='Banktypecode', blank=True, null=True)  # Field name made lowercase.
    iban = models.CharField(db_column='IBAN', max_length=26, blank=True, null=True)  # Field name made lowercase.
    owner = models.IntegerField(db_column='Owner')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Staff'


class Stafffamily(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    staffcode = models.ForeignKey(Staff, on_delete=models.DO_NOTHING, db_column='StaffCode')  # Field name made lowercase.
    type = models.SmallIntegerField(db_column='Type')  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=50)  # Field name made lowercase.
    sex = models.BooleanField(db_column='Sex')  # Field name made lowercase.
    insurancenumber = models.CharField(db_column='InsuranceNumber', max_length=20, blank=True, null=True)  # Field name made lowercase.
    birthdate = models.CharField(db_column='BirthDate', max_length=10, blank=True, null=True)  # Field name made lowercase.
    death = models.BooleanField(db_column='Death', blank=True, null=True)  # Field name made lowercase.
    deathdate = models.CharField(db_column='DeathDate', max_length=50, blank=True, null=True)  # Field name made lowercase.
    comment = models.CharField(db_column='Comment', max_length=500, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'StaffFamily'


class Staffgroup(models.Model):
    code = models.IntegerField(db_column='Code', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=50)  # Field name made lowercase.
    comment = models.CharField(db_column='Comment', max_length=500)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'StaffGroup'


class Staffoutput(models.Model):
    code = models.IntegerField(db_column='Code', primary_key=True)  # Field name made lowercase.
    salarybillcode = models.IntegerField(db_column='SalaryBillCode')  # Field name made lowercase.
    comment = models.CharField(db_column='Comment', max_length=500, blank=True, null=True)  # Field name made lowercase.
    staffcode = models.ForeignKey(Staff, on_delete=models.DO_NOTHING, db_column='StaffCode')  # Field name made lowercase.
    fromdate = models.CharField(db_column='fromDate', max_length=10)  # Field name made lowercase.
    todate = models.CharField(db_column='ToDate', max_length=10)  # Field name made lowercase.
    output = models.IntegerField(db_column='OutPut')  # Field name made lowercase.
    createdtime = models.CharField(db_column='CreatedTime', max_length=5, blank=True, null=True)  # Field name made lowercase.
    createddate = models.CharField(db_column='CreatedDate', max_length=10, blank=True, null=True)  # Field name made lowercase.
    modifiedtime = models.CharField(db_column='ModifiedTime', max_length=5, blank=True, null=True)  # Field name made lowercase.
    modifieddate = models.CharField(db_column='ModifiedDate', max_length=10, blank=True, null=True)  # Field name made lowercase.
    usercreated = models.CharField(db_column='UserCreated', max_length=50, blank=True, null=True)  # Field name made lowercase.
    usermodified = models.CharField(db_column='UserModified', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'StaffOutPut'


class Staffoutputdetail(models.Model):
    outputcode = models.ForeignKey(Staffoutput, on_delete=models.DO_NOTHING, db_column='OutPutCode')  # Field name made lowercase.
    amount = models.DecimalField(db_column='Amount', max_digits=23, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    type = models.BooleanField(db_column='Type')  # Field name made lowercase.
    itemcode = models.IntegerField(db_column='ItemCode')  # Field name made lowercase.
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'StaffOutPutDetail'


class Statements(models.Model):
    code = models.IntegerField(db_column='Code', primary_key=True, db_comment='کد صورتحساب')  # Field name made lowercase.
    statementtype = models.SmallIntegerField(db_column='StatementType', db_comment='نوع تفضيلي')  # Field name made lowercase.
    accdetailsref = models.IntegerField(db_column='AccDetailsRef', db_comment='کد تفضيلي')  # Field name made lowercase.
    totalcoderef = models.IntegerField(db_column='TotalCodeRef', blank=True, null=True, db_comment='کد کل')  # Field name made lowercase.
    assistantcoderef = models.IntegerField(db_column='AssistantCodeRef', blank=True, null=True, db_comment='کد معين')  # Field name made lowercase.
    projectscoderef = models.IntegerField(db_column='ProjectsCodeRef', blank=True, null=True, db_comment='کد مرکز هزينه')  # Field name made lowercase.
    sitbgprd = models.SmallIntegerField(db_column='SitBgPrd', blank=True, null=True, db_comment='بدهکار/بستانکار')  # Field name made lowercase.
    begininginventory = models.DecimalField(db_column='BeginingInventory', max_digits=23, decimal_places=8, db_comment='موجودي اول دوره')  # Field name made lowercase.
    curcode = models.IntegerField(db_column='CurCode', db_comment='نوع ارز')  # Field name made lowercase.
    iscomplete = models.SmallIntegerField(db_column='IsComplete', blank=True, null=True)  # Field name made lowercase.
    des = models.CharField(db_column='Des', max_length=500, blank=True, null=True, db_comment='شرح')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Statements'


class Statementsdet(models.Model):
    id = models.IntegerField(primary_key=True, db_comment='کليد اصلي')  # The composite primary key (id, IsTemp) found, that is not supported. The first column is selected.
    type = models.SmallIntegerField(db_column='Type', db_comment='بانک/سيستم')  # Field name made lowercase.
    statementsref = models.ForeignKey(Statements, on_delete=models.DO_NOTHING, db_column='StatementsRef', blank=True, null=True, db_comment='کليد فرعي صورتحساب')  # Field name made lowercase.
    sanad_code = models.CharField(db_column='Sanad_Code', max_length=50, blank=True, null=True, db_comment='شماره سند')  # Field name made lowercase.
    sanad_type = models.IntegerField(db_column='Sanad_Type', blank=True, null=True, db_comment='نوع سند')  # Field name made lowercase.
    date = models.CharField(db_column='Date', max_length=10, db_comment='تاريخ سند')  # Field name made lowercase.
    bed = models.DecimalField(db_column='Bed', max_digits=23, decimal_places=8, blank=True, null=True, db_comment='بد')  # Field name made lowercase.
    bes = models.DecimalField(db_column='Bes', max_digits=23, decimal_places=8, blank=True, null=True, db_comment='بس')  # Field name made lowercase.
    des = models.CharField(db_column='Des', max_length=500, blank=True, null=True, db_comment='شرح')  # Field name made lowercase.
    status = models.SmallIntegerField(db_column='Status', db_comment='وضعيت')  # Field name made lowercase.
    ismodifysanad = models.SmallIntegerField(db_column='IsModifySanad', db_comment='موقت/اصلي')  # Field name made lowercase.
    istemp = models.SmallIntegerField(db_column='IsTemp', db_comment='موقت/اصلي')  # Field name made lowercase.
    com_index = models.IntegerField(db_column='Com_Index', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'StatementsDet'
        unique_together = (('id', 'istemp'),)


class Stores(models.Model):
    code = models.SmallIntegerField(db_column='Code', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=50, blank=True, null=True)  # Field name made lowercase.
    comment = models.CharField(db_column='Comment', max_length=500, blank=True, null=True)  # Field name made lowercase.
    mogodi = models.DecimalField(db_column='Mogodi', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return self.name if self.name else f"انبار کد {self.code}"

    class Meta:
        managed = False
        db_table = 'Stores'


class Tcheckamani(models.Model):
    id_check = models.CharField(db_column='ID_Check', max_length=50)  # Field name made lowercase. The composite primary key (ID_Check, Type) found, that is not supported. The first column is selected.
    percode = models.IntegerField(db_column='PerCode', blank=True, null=True)  # Field name made lowercase.
    bankname = models.CharField(db_column='BankName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    bankshobe = models.CharField(db_column='BankShobe', max_length=50, blank=True, null=True)  # Field name made lowercase.
    bankid_h = models.CharField(db_column='BankID_H', max_length=50, blank=True, null=True)  # Field name made lowercase.
    amount = models.DecimalField(db_column='Amount', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    status = models.SmallIntegerField(db_column='Status', blank=True, null=True)  # Field name made lowercase.
    type = models.SmallIntegerField(db_column='Type')  # Field name made lowercase.
    bankcode = models.IntegerField(db_column='BankCode', blank=True, null=True)  # Field name made lowercase.
    operationdate = models.CharField(db_column='OperationDate', max_length=10, blank=True, null=True)  # Field name made lowercase.
    date = models.CharField(db_column='Date', max_length=10, blank=True, null=True)  # Field name made lowercase.
    radif = models.IntegerField(db_column='Radif', blank=True, null=True)  # Field name made lowercase.
    comments = models.CharField(db_column='Comments', max_length=500, blank=True, null=True)  # Field name made lowercase.
    vouchercode = models.IntegerField(db_column='VoucherCode', blank=True, null=True)  # Field name made lowercase.
    loancode = models.IntegerField(db_column='LoanCode', blank=True, null=True)  # Field name made lowercase.
    vouchercode_back = models.IntegerField(db_column='VoucherCode_Back', blank=True, null=True)  # Field name made lowercase.
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    returndate = models.CharField(db_column='ReturnDate', max_length=10, blank=True, null=True)  # Field name made lowercase.
    createdtime = models.CharField(db_column='CreatedTime', max_length=5)  # Field name made lowercase.
    createddate = models.CharField(db_column='CreatedDate', max_length=10)  # Field name made lowercase.
    modifiedtime = models.CharField(db_column='ModifiedTime', max_length=5, blank=True, null=True)  # Field name made lowercase.
    modifieddate = models.CharField(db_column='ModifiedDate', max_length=10, blank=True, null=True)  # Field name made lowercase.
    usercreated = models.IntegerField(db_column='UserCreated')  # Field name made lowercase.
    usermodified = models.IntegerField(db_column='UserModified', blank=True, null=True)  # Field name made lowercase.
    owner = models.IntegerField(db_column='Owner')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TCheckAmani'
        unique_together = (('id_check', 'type'),)


class TempBackfactVisitor(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    backfact_code = models.IntegerField(db_column='BackFact_code', blank=True, null=True)  # Field name made lowercase.
    per_code = models.IntegerField(db_column='Per_code', blank=True, null=True)  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sellfactvisitori = models.DecimalField(db_column='SellFactVisitori', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    percent = models.DecimalField(db_column='Percent', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    price = models.DecimalField(db_column='Price', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    tmp = models.BooleanField(blank=True, null=True)
    type_pay = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TEMP_backFact_Visitor'


class Tkalaamani(models.Model):
    code = models.IntegerField(db_column='Code', primary_key=True)  # Field name made lowercase.
    percode = models.IntegerField(db_column='PerCode', blank=True, null=True)  # Field name made lowercase.
    status = models.SmallIntegerField(db_column='Status', blank=True, null=True)  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=10, blank=True, null=True)  # Field name made lowercase.
    kalacode = models.IntegerField(db_column='kalaCode', blank=True, null=True)  # Field name made lowercase.
    date = models.CharField(db_column='Date', max_length=10, blank=True, null=True)  # Field name made lowercase.
    comment = models.CharField(db_column='Comment', max_length=500, blank=True, null=True)  # Field name made lowercase.
    meghdar = models.DecimalField(db_column='Meghdar', max_digits=23, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    operation_date = models.CharField(db_column='Operation_Date', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TKalaAmani'


class TmpbankGar(models.Model):
    code = models.CharField(db_column='Code', max_length=50)  # Field name made lowercase.
    percode = models.IntegerField(db_column='PerCode')  # Field name made lowercase.
    type = models.SmallIntegerField(db_column='Type')  # Field name made lowercase.
    date = models.CharField(db_column='Date', max_length=10, blank=True, null=True)  # Field name made lowercase.
    sanad_code = models.IntegerField(db_column='Sanad_Code', blank=True, null=True)  # Field name made lowercase.
    type_gar = models.SmallIntegerField(db_column='Type_Gar')  # Field name made lowercase.
    amount = models.DecimalField(db_column='Amount', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TMPBank_Gar'


class Tmpgar(models.Model):
    code = models.CharField(db_column='Code', max_length=50, blank=True, null=True)  # Field name made lowercase.
    type = models.SmallIntegerField(db_column='Type', blank=True, null=True)  # Field name made lowercase.
    date = models.CharField(db_column='Date', max_length=10, blank=True, null=True)  # Field name made lowercase.
    sanad_code = models.SmallIntegerField(db_column='Sanad_Code', blank=True, null=True)  # Field name made lowercase.
    amount = models.DecimalField(db_column='Amount', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    megh = models.IntegerField(db_column='Megh', blank=True, null=True)  # Field name made lowercase.
    kala_code = models.IntegerField(db_column='Kala_Code', blank=True, null=True)  # Field name made lowercase.
    vaz = models.SmallIntegerField(db_column='Vaz', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TMPGar'


class Tmpstaffdeduction(models.Model):
    id =  models.AutoField(db_column='ID', primary_key=True) # Field name made lowercase.
    staffcode = models.IntegerField(db_column='StaffCode')  # Field name made lowercase.
    itemcode = models.IntegerField(db_column='ItemCode')  # Field name made lowercase.
    cost = models.DecimalField(db_column='Cost', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TMPStaffDeduction'


class Tmpstafffamily(models.Model):
    id = models.IntegerField(db_column='ID',primary_key=True)  # Field name made lowercase.
    staffcode = models.IntegerField(db_column='StaffCode')  # Field name made lowercase.
    type = models.SmallIntegerField(db_column='Type')  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=50)  # Field name made lowercase.
    sex = models.BooleanField(db_column='Sex')  # Field name made lowercase.
    insurancenumber = models.CharField(db_column='InsuranceNumber', max_length=20, blank=True, null=True)  # Field name made lowercase.
    birthdate = models.CharField(db_column='BirthDate', max_length=10, blank=True, null=True)  # Field name made lowercase.
    death = models.BooleanField(db_column='Death', blank=True, null=True)  # Field name made lowercase.
    deathdate = models.CharField(db_column='DeathDate', max_length=50, blank=True, null=True)  # Field name made lowercase.
    comment = models.CharField(db_column='Comment', max_length=500, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TMPStaffFamily'


class Tmpstafffiscal(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    staffcode = models.IntegerField(db_column='StaffCode')  # Field name made lowercase.
    itemcode = models.IntegerField(db_column='ItemCode')  # Field name made lowercase.
    cost = models.DecimalField(db_column='Cost', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TMPStaffFiscal'


class Tmpstaffsalary(models.Model):
    staffcode = models.IntegerField(db_column='StaffCode')  # Field name made lowercase.
    entrance = models.CharField(db_column='Entrance', max_length=5, blank=True, null=True)  # Field name made lowercase.
    exit = models.CharField(db_column='Exit', max_length=5, blank=True, null=True)  # Field name made lowercase.
    output = models.IntegerField(db_column='Output', blank=True, null=True)  # Field name made lowercase.
    weekendoutput = models.DecimalField(db_column='WeekEndOutPut', max_digits=23, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    salary = models.DecimalField(db_column='Salary', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    leavepay = models.DecimalField(db_column='LeavePay', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    dutypay = models.DecimalField(db_column='DutyPay', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    overtimepay = models.DecimalField(db_column='OvertimePay', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    discount = models.DecimalField(db_column='Discount', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    discounttype = models.SmallIntegerField(db_column='DiscountType')  # Field name made lowercase.
    absence = models.DecimalField(db_column='Absence', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    weekendentrance = models.CharField(db_column='WeekEndEntrance', max_length=5, blank=True, null=True)  # Field name made lowercase.
    weekendexit = models.CharField(db_column='WeekEndExit', max_length=5, blank=True, null=True)  # Field name made lowercase.
    leaveceil = models.CharField(db_column='LeaveCeil', max_length=5, blank=True, null=True)  # Field name made lowercase.
    holiday = models.DecimalField(db_column='Holiday', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    late = models.DecimalField(db_column='Late', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    lateeffect = models.SmallIntegerField(db_column='LateEffect', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TMPStaffSalary'


class Tmptbl(models.Model):
    hours = models.CharField(db_column='Hours', max_length=10, blank=True, null=True)  # Field name made lowercase.
    minutes = models.CharField(max_length=10, blank=True, null=True)
    seconds = models.CharField(max_length=10, blank=True, null=True)
    code = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TMPTBL'


class TmpFactVisitor(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    fact_code = models.IntegerField(blank=True, null=True)
    per_code = models.IntegerField(db_column='Per_code', blank=True, null=True)  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=50, blank=True, null=True)  # Field name made lowercase.
    percent = models.DecimalField(db_column='Percent', max_digits=23, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    price = models.DecimalField(db_column='Price', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    tmp = models.BooleanField(blank=True, null=True)
    type_pay = models.BooleanField(blank=True, null=True)
    currtype = models.BooleanField(db_column='CurrType', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TMP_Fact_Visitor'


class TmpPayrecieveVisitor(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    fact_code = models.IntegerField(blank=True, null=True)
    per_code = models.IntegerField(db_column='Per_code', blank=True, null=True)  # Field name made lowercase.
    tmp = models.BooleanField(blank=True, null=True)
    fact_tmp = models.BooleanField(db_column='Fact_TMP', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TMP_PayRecieve_Visitor'


class TmpWorktimeMap(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=100, blank=True, null=True)  # Field name made lowercase.
    comment = models.CharField(db_column='Comment', max_length=400, blank=True, null=True)  # Field name made lowercase.
    default = models.BooleanField(db_column='Default', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TMP_WorkTime_Map'


class TmpWorktimeMapdetail(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    mapcode = models.IntegerField(db_column='MapCode', blank=True, null=True)  # Field name made lowercase.
    item_type = models.BooleanField(db_column='Item_Type', blank=True, null=True)  # Field name made lowercase.
    item_code = models.IntegerField(db_column='Item_Code', blank=True, null=True)  # Field name made lowercase.
    column_name = models.CharField(db_column='Column_Name', max_length=250, blank=True, null=True)  # Field name made lowercase.
    comment = models.CharField(db_column='Comment', max_length=500, blank=True, null=True)  # Field name made lowercase.
    type_100 = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TMP_WorkTime_MapDetail'


class TmpBackfactVisitor(models.Model):
    id = id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    backfact_code = models.IntegerField(db_column='BackFact_code', blank=True, null=True)  # Field name made lowercase.
    per_code = models.IntegerField(db_column='Per_code', blank=True, null=True)  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=50, blank=True, null=True)  # Field name made lowercase.
    percent = models.DecimalField(db_column='Percent', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    price = models.DecimalField(db_column='Price', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    tmp = models.BooleanField(blank=True, null=True)
    type_pay = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TMP_backFact_Visitor'


class TmpPerfactVisitor(models.Model):
    id = id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    fact_code = models.IntegerField(blank=True, null=True)
    per_code = models.IntegerField(db_column='Per_code', blank=True, null=True)  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=50, blank=True, null=True)  # Field name made lowercase.
    percent = models.DecimalField(db_column='Percent', max_digits=23, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    price = models.DecimalField(db_column='Price', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    tmp = models.BooleanField(blank=True, null=True)
    type_pay = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TMP_perFact_Visitor'


class Tab(models.Model):
    code = models.IntegerField(db_column='Code')  # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=50)  # Field name made lowercase.
    managetype = models.SmallIntegerField(db_column='ManageType', blank=True, null=True)  # Field name made lowercase.
    usercode = models.IntegerField(db_column='UserCode', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Tab'


class Tablesfieldslist(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True, db_comment='کليد اصلي')  # Field name made lowercase.
    tableslistid = models.ForeignKey('Tableslist', on_delete=models.DO_NOTHING, db_column='TablesListID', db_comment='کليد فرعي ليست جداول')  # Field name made lowercase.
    fieldname = models.CharField(db_column='FieldName', max_length=128, db_comment='نام فيلد')  # Field name made lowercase.
    fieldcaption = models.CharField(db_column='FieldCaption', max_length=500, db_comment='کپشن فيلد')  # Field name made lowercase.
    comment = models.CharField(db_column='Comment', max_length=500, blank=True, null=True, db_comment='توضيحات')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TablesFieldsList'


class Tableslist(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True, db_comment='کليد اصلي')  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=128, db_comment='نام جدول')  # Field name made lowercase.
    caption = models.CharField(db_column='Caption', max_length=500, db_comment='کپشن جدول')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TablesList'


class Tags(models.Model):
    code = models.IntegerField(db_column='Code', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=50, blank=True, null=True)  # Field name made lowercase.
    color_code = models.CharField(max_length=20, blank=True, null=True)
    isdeleted = models.BooleanField(db_column='ISDeleted', blank=True, null=True)  # Field name made lowercase.
    create_date = models.CharField(db_column='Create_Date', max_length=20, blank=True, null=True)  # Field name made lowercase.
    modify_date = models.CharField(db_column='Modify_Date', max_length=20, blank=True, null=True)  # Field name made lowercase.
    create_user = models.IntegerField(db_column='Create_User', blank=True, null=True)  # Field name made lowercase.
    modify_user = models.IntegerField(db_column='Modify_User', blank=True, null=True)  # Field name made lowercase.
    enable = models.BooleanField(db_column='Enable', blank=True, null=True)  # Field name made lowercase.
    comment = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TagS'


class Tax(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    fromsalary = models.DecimalField(db_column='FromSalary', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    tosalary = models.DecimalField(db_column='ToSalary', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    comment = models.CharField(db_column='Comment', max_length=500, blank=True, null=True)  # Field name made lowercase.
    percent = models.DecimalField(db_column='Percent', max_digits=23, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    taxmaincode = models.ForeignKey('Taxmain', on_delete=models.DO_NOTHING, db_column='TaxMainCode')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Tax'


class Taxmain(models.Model):
    code = models.IntegerField(db_column='Code', primary_key=True)  # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=50)  # Field name made lowercase.
    comment = models.CharField(db_column='Comment', max_length=500, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TaxMain'


class Tempmiangin(models.Model):
    radif = models.BigIntegerField(db_column='RADIF', blank=True, null=True)  # Field name made lowercase.
    date = models.CharField(db_column='DATE', max_length=10, blank=True, null=True)  # Field name made lowercase.
    miangin = models.DecimalField(db_column='MIANGIN', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    bagh = models.DecimalField(db_column='BAGH', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TempMiangin'


class TempTaf(models.Model):
    date = models.CharField(db_column='Date', max_length=10, blank=True, null=True)  # Field name made lowercase.
    bes = models.DecimalField(db_column='Bes', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    bed = models.DecimalField(db_column='Bed', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    bagh = models.DecimalField(db_column='Bagh', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    sharh = models.CharField(db_column='Sharh', max_length=500, blank=True, null=True)  # Field name made lowercase.
    vahed = models.CharField(db_column='Vahed', max_length=20, blank=True, null=True)  # Field name made lowercase.
    gheymat = models.DecimalField(db_column='Gheymat', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    tashkhis = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Temp_Taf'


class Tipoftheday(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    text = models.CharField(db_column='Text', max_length=500, blank=True, null=True)  # Field name made lowercase.
    showcount = models.SmallIntegerField(db_column='ShowCount', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TipOfTheDay'


class TmpassignmentPay(models.Model):
    id = models.IntegerField(db_column='ID',primary_key=True)  # Field name made lowercase.
    assignmentdate = models.CharField(db_column='AssignmentDate', max_length=10, blank=True, null=True)  # Field name made lowercase.
    assignmentnum = models.CharField(db_column='AssignmentNum', max_length=30, blank=True, null=True)  # Field name made lowercase.
    cost = models.DecimalField(db_column='Cost', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=200, blank=True, null=True)  # Field name made lowercase.
    entitycode = models.IntegerField(db_column='EntityCode', blank=True, null=True)  # Field name made lowercase.
    entitytype = models.BooleanField(db_column='EntityType', blank=True, null=True)  # Field name made lowercase.
    bankname = models.CharField(db_column='BankName', max_length=30, blank=True, null=True)  # Field name made lowercase.
    bankbranch = models.CharField(db_column='BankBranch', max_length=30, blank=True, null=True)  # Field name made lowercase.
    accountid = models.CharField(db_column='AccountID', max_length=30, blank=True, null=True)  # Field name made lowercase.
    sanadcode = models.IntegerField(db_column='SanadCode', blank=True, null=True)  # Field name made lowercase.
    currcode = models.IntegerField(db_column='CurrCode', blank=True, null=True)  # Field name made lowercase.
    currrate = models.DecimalField(db_column='CurrRate', max_digits=23, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    bankwagecode = models.IntegerField(db_column='BankWageCode', blank=True, null=True)  # Field name made lowercase.
    bankwagecost = models.DecimalField(db_column='BankWageCost', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TmpAssignment_Pay'


class TmpassignmentRecieve(models.Model):
    id = models.IntegerField(db_column='ID',primary_key=True)  # Field name made lowercase.
    assignmentdate = models.CharField(db_column='AssignmentDate', max_length=10, blank=True, null=True)  # Field name made lowercase.
    assignmentnum = models.CharField(db_column='AssignmentNum', max_length=50, blank=True, null=True)  # Field name made lowercase.
    cost = models.DecimalField(db_column='Cost', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=200, blank=True, null=True)  # Field name made lowercase.
    bankcode = models.IntegerField(db_column='BankCode', blank=True, null=True)  # Field name made lowercase.
    sanadcode = models.IntegerField(db_column='SanadCode', blank=True, null=True)  # Field name made lowercase.
    flag = models.SmallIntegerField(blank=True, null=True)
    currcode = models.IntegerField(db_column='CurrCode', blank=True, null=True)  # Field name made lowercase.
    currrate = models.DecimalField(db_column='CurrRate', max_digits=23, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    tmp = models.SmallIntegerField(db_column='Tmp', blank=True, null=True)  # Field name made lowercase.
    assignmenttype = models.SmallIntegerField(db_column='AssignmentType')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TmpAssignment_Recieve'


class Tmpchequepay(models.Model):
    id = models.IntegerField(db_column='ID', blank=True, primary_key=True)  # Field name made lowercase.
    chequeid = models.CharField(db_column='ChequeID', max_length=30, blank=True, null=True)  # Field name made lowercase.
    chequerow = models.IntegerField(db_column='ChequeRow', blank=True, null=True)  # Field name made lowercase.
    issuancedate = models.CharField(db_column='IssuanceDate', max_length=10, blank=True, null=True)  # Field name made lowercase.
    chequedate = models.CharField(db_column='ChequeDate', max_length=10, blank=True, null=True)  # Field name made lowercase.
    cost = models.DecimalField(db_column='Cost', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    bankcode = models.IntegerField(db_column='BankCode', blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=200, blank=True, null=True)  # Field name made lowercase.
    status = models.IntegerField(blank=True, null=True)
    firstperiod = models.BooleanField(db_column='FirstPeriod', blank=True, null=True)  # Field name made lowercase.
    chequeidcounter = models.IntegerField(db_column='ChequeIDCounter', blank=True, null=True)  # Field name made lowercase.
    operationcode = models.IntegerField(db_column='OperationCode', blank=True, null=True)  # Field name made lowercase.
    operationtype = models.BooleanField(db_column='OperationType', blank=True, null=True)  # Field name made lowercase.
    vouchercode = models.IntegerField(db_column='VoucherCode', blank=True, null=True)  # Field name made lowercase.
    location = models.CharField(db_column='Location', max_length=50, blank=True, null=True)  # Field name made lowercase.
    locationcomment = models.CharField(db_column='LocationComment', max_length=500, blank=True, null=True)  # Field name made lowercase.
    percode = models.IntegerField(db_column='PerCode', blank=True, null=True)  # Field name made lowercase.
    recievestatus = models.IntegerField(db_column='RecieveStatus', blank=True, null=True)  # Field name made lowercase.
    currcode = models.IntegerField(db_column='CurrCode', blank=True, null=True)  # Field name made lowercase.
    currrate = models.DecimalField(db_column='CurrRate', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    usercreated = models.IntegerField(db_column='UserCreated')  # Field name made lowercase.
    createdtime = models.CharField(db_column='CreatedTime', max_length=5)  # Field name made lowercase.
    createddate = models.CharField(db_column='CreatedDate', max_length=10)  # Field name made lowercase.
    modifiedtime = models.CharField(db_column='ModifiedTime', max_length=5, blank=True, null=True)  # Field name made lowercase.
    modifieddate = models.CharField(db_column='ModifiedDate', max_length=10, blank=True, null=True)  # Field name made lowercase.
    usermodified = models.IntegerField(db_column='UserModified', blank=True, null=True)  # Field name made lowercase.
    owner = models.IntegerField(db_column='Owner')  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TmpChequePay'


class TmpchequesRecieve(models.Model):
    id = models.IntegerField(db_column='ID',primary_key=True)  # Field name made lowercase.
    chequeid = models.CharField(db_column='ChequeID', max_length=30)  # Field name made lowercase.
    chequerow = models.IntegerField(db_column='CHequeRow', blank=True, null=True)  # Field name made lowercase.
    issuancedate = models.CharField(db_column='IssuanceDate', max_length=10, blank=True, null=True)  # Field name made lowercase.
    chequedate = models.CharField(db_column='ChequeDate', max_length=10, blank=True, null=True)  # Field name made lowercase.
    cost = models.DecimalField(db_column='Cost', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    bankname = models.CharField(db_column='BankName', max_length=50)  # Field name made lowercase.
    bankbranch = models.CharField(db_column='BankBranch', max_length=50, blank=True, null=True)  # Field name made lowercase.
    accountid = models.CharField(db_column='AccountID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=200, blank=True, null=True)  # Field name made lowercase.
    status = models.SmallIntegerField(db_column='Status')  # Field name made lowercase.
    operationcode = models.IntegerField(db_column='OperationCode', blank=True, null=True)  # Field name made lowercase.
    vouchercode = models.IntegerField(db_column='VoucherCode', blank=True, null=True)  # Field name made lowercase.
    location = models.CharField(db_column='Location', max_length=30, blank=True, null=True)  # Field name made lowercase.
    locationcomment = models.CharField(db_column='LocationComment', max_length=500, blank=True, null=True)  # Field name made lowercase.
    percode = models.IntegerField(db_column='PerCode', blank=True, null=True)  # Field name made lowercase.
    firstperiod = models.BooleanField(db_column='FirstPeriod', blank=True, null=True)  # Field name made lowercase.
    operationtype = models.IntegerField(db_column='OperationType', blank=True, null=True)  # Field name made lowercase.
    chequeidcounter = models.SmallIntegerField(db_column='ChequeIDCounter', blank=True, null=True)  # Field name made lowercase.
    currcode = models.IntegerField(db_column='CurrCode', blank=True, null=True)  # Field name made lowercase.
    currrate = models.DecimalField(db_column='CurrRate', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    entitycode = models.IntegerField(db_column='EntityCode', blank=True, null=True)  # Field name made lowercase.
    iban = models.CharField(db_column='IBAN', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sayadid = models.CharField(db_column='SayadId', max_length=50, blank=True, null=True)  # Field name made lowercase.
    usercreated = models.IntegerField(db_column='UserCreated')  # Field name made lowercase.
    createdtime = models.CharField(db_column='CreatedTime', max_length=5)  # Field name made lowercase.
    createddate = models.CharField(db_column='CreatedDate', max_length=10)  # Field name made lowercase.
    modifiedtime = models.CharField(db_column='ModifiedTime', max_length=5, blank=True, null=True)  # Field name made lowercase.
    modifieddate = models.CharField(db_column='ModifiedDate', max_length=10, blank=True, null=True)  # Field name made lowercase.
    usermodified = models.IntegerField(db_column='UserModified', blank=True, null=True)  # Field name made lowercase.
    owner = models.IntegerField(db_column='Owner')  # Field name made lowercase.
    tmp = models.SmallIntegerField(db_column='Tmp', blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TmpCheques_Recieve'


class Tmpgardeshbank(models.Model):
    date = models.CharField(db_column='Date', max_length=10, blank=True, null=True)  # Field name made lowercase.
    comment = models.CharField(db_column='Comment', max_length=500, blank=True, null=True)  # Field name made lowercase.
    bes = models.DecimalField(db_column='Bes', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    bed = models.DecimalField(db_column='Bed', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    bagh = models.DecimalField(db_column='Bagh', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=50, blank=True, null=True)  # Field name made lowercase.
    type = models.SmallIntegerField(db_column='Type', blank=True, null=True)  # Field name made lowercase.
    radif = models.BigIntegerField(db_column='Radif', blank=True, null=True)  # Field name made lowercase.
    code = models.CharField(db_column='Code', max_length=50, blank=True, null=True)  # Field name made lowercase.
    vouchercode = models.IntegerField(db_column='VoucherCode', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TmpGardeshBank'


class Tmpgardeshdaramad(models.Model):
    date = models.CharField(db_column='Date', max_length=10, blank=True, null=True)  # Field name made lowercase.
    comment = models.CharField(db_column='Comment', max_length=500, blank=True, null=True)  # Field name made lowercase.
    bes = models.DecimalField(db_column='Bes', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    bed = models.DecimalField(db_column='Bed', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    bagh = models.DecimalField(db_column='Bagh', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=50, blank=True, null=True)  # Field name made lowercase.
    type = models.SmallIntegerField(db_column='Type', blank=True, null=True)  # Field name made lowercase.
    radif = models.BigIntegerField(db_column='Radif', blank=True, null=True)  # Field name made lowercase.
    code = models.CharField(db_column='Code', max_length=50, blank=True, null=True)  # Field name made lowercase.
    vouchercode = models.IntegerField(db_column='VoucherCode', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TmpGardeshDaramad'


class Tmpgardeshhazine(models.Model):
    date = models.CharField(db_column='Date', max_length=10, blank=True, null=True)  # Field name made lowercase.
    comment = models.CharField(db_column='Comment', max_length=500, blank=True, null=True)  # Field name made lowercase.
    bes = models.DecimalField(db_column='Bes', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    bed = models.DecimalField(db_column='Bed', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    bagh = models.DecimalField(db_column='Bagh', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=50, blank=True, null=True)  # Field name made lowercase.
    type = models.SmallIntegerField(db_column='Type', blank=True, null=True)  # Field name made lowercase.
    radif = models.BigIntegerField(db_column='Radif', blank=True, null=True)  # Field name made lowercase.
    code = models.CharField(db_column='Code', max_length=50, blank=True, null=True)  # Field name made lowercase.
    vouchercode = models.IntegerField(db_column='VoucherCode', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TmpGardeshHazine'


class Tmpgardeshsandogh(models.Model):
    date = models.CharField(db_column='Date', max_length=10, blank=True, null=True)  # Field name made lowercase.
    comment = models.CharField(db_column='Comment', max_length=500, blank=True, null=True)  # Field name made lowercase.
    bes = models.DecimalField(db_column='Bes', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    bed = models.DecimalField(db_column='Bed', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    bagh = models.DecimalField(db_column='Bagh', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=50, blank=True, null=True)  # Field name made lowercase.
    type = models.SmallIntegerField(db_column='Type', blank=True, null=True)  # Field name made lowercase.
    radif = models.BigIntegerField(db_column='Radif', blank=True, null=True)  # Field name made lowercase.
    code = models.CharField(db_column='Code', max_length=50, blank=True, null=True)  # Field name made lowercase.
    vouchercode = models.IntegerField(db_column='VoucherCode', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TmpGardeshSandogh'


class Tmpgardeshtafsili(models.Model):
    radif = models.BigIntegerField(db_column='Radif', blank=True, null=True)  # Field name made lowercase.
    date = models.CharField(db_column='Date', max_length=10, blank=True, null=True)  # Field name made lowercase.
    comment = models.CharField(db_column='Comment', max_length=500, blank=True, null=True)  # Field name made lowercase.
    meghdar = models.DecimalField(db_column='Meghdar', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    units = models.CharField(db_column='Units', max_length=50, blank=True, null=True)  # Field name made lowercase.
    naghdi = models.DecimalField(db_column='Naghdi', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    bes = models.DecimalField(db_column='Bes', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    bed = models.DecimalField(db_column='Bed', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    mandeh = models.DecimalField(db_column='Mandeh', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=50, blank=True, null=True)  # Field name made lowercase.
    taxcharge = models.DecimalField(db_column='TaxCharge', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    vouchercode = models.IntegerField(db_column='VoucherCode', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TmpGardeshTafsili'


class TmpkharidDetail(models.Model):
    code = models.IntegerField(primary_key=True)  # The composite primary key (code, radif) found, that is not supported. The first column is selected.
    radif = models.SmallIntegerField()
    an_code = models.ForeignKey(Stores, on_delete=models.DO_NOTHING, db_column='an_code', blank=True, null=True)
    kala_code = models.IntegerField()
    sharh = models.CharField(max_length=500, blank=True, null=True)
    meghdar = models.DecimalField(max_digits=23, decimal_places=8, blank=True, null=True)
    naghdi = models.DecimalField(max_digits=23, decimal_places=9, blank=True, null=True)
    reval = models.IntegerField(blank=True, null=True)
    haml = models.DecimalField(max_digits=23, decimal_places=9, blank=True, null=True)
    sh_mashin = models.CharField(max_length=50, blank=True, null=True)
    sh_barnameh = models.CharField(max_length=50, blank=True, null=True)
    code_driver = models.IntegerField(blank=True, null=True)
    status = models.SmallIntegerField(db_column='Status', blank=True, null=True)  # Field name made lowercase.
    vaziyat = models.SmallIntegerField()
    type = models.SmallIntegerField(db_column='Type', blank=True, null=True)  # Field name made lowercase.
    tool = models.DecimalField(max_digits=23, decimal_places=8, blank=True, null=True)
    arz = models.DecimalField(max_digits=23, decimal_places=8, blank=True, null=True)
    tedad = models.IntegerField(blank=True, null=True)
    meghdar2 = models.DecimalField(max_digits=23, decimal_places=8, blank=True, null=True)
    bestype = models.SmallIntegerField(db_column='BesType', blank=True, null=True)  # Field name made lowercase.
    bedtype = models.SmallIntegerField(db_column='BedType', blank=True, null=True)  # Field name made lowercase.
    com_index = models.IntegerField()
    chargepercent = models.DecimalField(db_column='ChargePercent', max_digits=23, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    taxpercent = models.DecimalField(db_column='TaxPercent', max_digits=23, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    hazinecomment = models.CharField(db_column='HazineComment', max_length=500, blank=True, null=True)  # Field name made lowercase.
    hazinecode = models.IntegerField(db_column='HazineCode', blank=True, null=True)  # Field name made lowercase.
    takhfif = models.DecimalField(max_digits=23, decimal_places=9, blank=True, null=True)
    takhfif_type = models.BooleanField(db_column='Takhfif_Type', blank=True, null=True)  # Field name made lowercase.
    off_user = models.DecimalField(db_column='Off_User', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    off_sys = models.DecimalField(db_column='Off_Sys', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    cost_entery_type = models.BooleanField(db_column='Cost_Entery_Type', blank=True, null=True)  # Field name made lowercase.
    totalcost = models.DecimalField(db_column='TotalCost', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    currcode = models.IntegerField(db_column='CurrCode', blank=True, null=True)  # Field name made lowercase.
    currrate = models.DecimalField(db_column='CurrRate', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    takhfif_costtype = models.BooleanField(db_column='Takhfif_CostType', blank=True, null=True)  # Field name made lowercase.
    ordercode = models.IntegerField(db_column='OrderCode', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TmpKharid_detail'
        unique_together = (('code', 'radif'),)


class Tmpletterdetail(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    lettercode = models.IntegerField(db_column='LetterCode')  # Field name made lowercase.
    person = models.CharField(db_column='Person', max_length=50)  # Field name made lowercase.
    referplace = models.CharField(db_column='ReferPlace', max_length=50, blank=True, null=True)  # Field name made lowercase.
    dodate = models.CharField(db_column='DoDate', max_length=10, blank=True, null=True)  # Field name made lowercase.
    docomment = models.CharField(db_column='DoComment', max_length=500, blank=True, null=True)  # Field name made lowercase.
    refercomment = models.CharField(db_column='ReferComment', max_length=500, blank=True, null=True)  # Field name made lowercase.
    referuserid = models.IntegerField(db_column='ReferUserId')  # Field name made lowercase.
    referdate = models.CharField(db_column='ReferDate', max_length=10)  # Field name made lowercase.
    refertime = models.CharField(db_column='ReferTime', max_length=5)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TmpLetterDetail'


class Tmprepairandholddetail(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    repairandholdcode = models.IntegerField(db_column='RepairAndHoldCode')  # Field name made lowercase.
    expensecode = models.IntegerField(db_column='ExpenseCode', blank=True, null=True)  # Field name made lowercase.
    expensetype = models.SmallIntegerField(db_column='ExpenseType')  # Field name made lowercase.
    cost = models.DecimalField(db_column='Cost', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    comment = models.CharField(db_column='Comment', max_length=500, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TmpRepairAndHoldDetail'


class Tmptax(models.Model):
    id = id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    taxmaincode = models.IntegerField(db_column='TaxMainCode')  # Field name made lowercase.
    fromsalary = models.DecimalField(db_column='FromSalary', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    tosalary = models.DecimalField(db_column='ToSalary', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    comment = models.CharField(db_column='Comment', max_length=500, blank=True, null=True)  # Field name made lowercase.
    percent = models.DecimalField(db_column='Percent', max_digits=23, decimal_places=8, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TmpTax'


class TmpTeraz(models.Model):
    jbed = models.DecimalField(max_digits=23, decimal_places=9, blank=True, null=True)
    jbes = models.DecimalField(max_digits=23, decimal_places=9, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Tmp_teraz'


class Toolfiles(models.Model):
    id = models.AutoField(primary_key=True)
    filecontent = models.BinaryField(db_column='FileContent')  # Field name made lowercase.
    filename = models.CharField(db_column='FileName', max_length=500, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ToolFiles'


class Toolid(models.Model):
    date = models.CharField(db_column='Date', max_length=10, blank=True, null=True)  # Field name made lowercase.
    ftoolid = models.IntegerField(db_column='FToolid', blank=True, null=True)  # Field name made lowercase.
    meghdar = models.DecimalField(db_column='Meghdar', max_digits=23, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    anbarfrom = models.IntegerField(db_column='AnbarFrom', blank=True, null=True)  # Field name made lowercase.
    anbarto = models.IntegerField(db_column='AnbarTo', blank=True, null=True)  # Field name made lowercase.
    mab_hazine = models.DecimalField(db_column='Mab_Hazine', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    mab_kol = models.DecimalField(db_column='Mab_Kol', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    comment = models.CharField(db_column='Comment', max_length=500, blank=True, null=True)  # Field name made lowercase.
    gheymat_vahed = models.DecimalField(db_column='Gheymat_Vahed', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    code = models.IntegerField(db_column='Code', primary_key=True)  # Field name made lowercase.
    vouchercode = models.IntegerField(db_column='VoucherCode', blank=True, null=True)  # Field name made lowercase.
    expcentercode = models.IntegerField(db_column='ExpCenterCode', blank=True, null=True)  # Field name made lowercase.
    global_field = models.ForeignKey(GlobalIds, on_delete=models.DO_NOTHING, db_column='Global_ID', blank=True, null=True)  # Field name made lowercase. Field renamed because it was a Python reserved word.

    class Meta:
        managed = False
        db_table = 'Toolid'


class ToolidDetail(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    toolid_code = models.IntegerField(db_column='Toolid_Code')  # Field name made lowercase.
    code = models.IntegerField(db_column='Code')  # Field name made lowercase.
    type = models.SmallIntegerField(db_column='Type')  # Field name made lowercase.
    meghdar = models.DecimalField(db_column='Meghdar', max_digits=23, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    mablagh = models.DecimalField(db_column='Mablagh', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    tmp = models.BooleanField()
    rowid = models.IntegerField(db_column='RowId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Toolid_Detail'


class ToolidDetailVar(models.Model):
    toolid_code = models.IntegerField(db_column='Toolid_Code', primary_key=True)  # Field name made lowercase. The composite primary key (Toolid_Code, Radif, tmp) found, that is not supported. The first column is selected.
    radif = models.SmallIntegerField(db_column='Radif')  # Field name made lowercase.
    kala_code = models.IntegerField(db_column='Kala_Code', blank=True, null=True)  # Field name made lowercase.
    meghdar = models.DecimalField(db_column='Meghdar', max_digits=23, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    tmp = models.SmallIntegerField()
    type = models.SmallIntegerField(db_column='Type', blank=True, null=True)  # Field name made lowercase.
    mablagh = models.DecimalField(db_column='Mablagh', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    com_index = models.IntegerField(db_column='Com_Index')  # Field name made lowercase.
    anbar = models.IntegerField(db_column='Anbar', blank=True, null=True)  # Field name made lowercase.
    meghdar2 = models.DecimalField(max_digits=23, decimal_places=8, blank=True, null=True)
    comment = models.CharField(db_column='Comment', max_length=500, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Toolid_Detail_Var'
        unique_together = (('toolid_code', 'radif', 'tmp'),)


class ToolidHaz(models.Model):
    code = models.IntegerField(db_column='Code')  # Field name made lowercase.
    name = models.IntegerField(db_column='Name', blank=True, null=True)  # Field name made lowercase.
    type = models.SmallIntegerField(db_column='Type', blank=True, null=True)  # Field name made lowercase.
    comment = models.CharField(db_column='Comment', max_length=500, blank=True, null=True)  # Field name made lowercase.
    mablagh = models.DecimalField(db_column='Mablagh', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    radif = models.SmallIntegerField(db_column='Radif', blank=True, null=True)  # Field name made lowercase.
    com_index = models.IntegerField(db_column='Com_Index')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Toolid_Haz'


class ToolidKala(models.Model):
    comment = models.CharField(db_column='Comment', max_length=500, blank=True, null=True)  # Field name made lowercase.
    kala_code = models.IntegerField(db_column='Kala_Code')  # Field name made lowercase.
    code = models.AutoField(db_column='Code', primary_key=True)  # Field name made lowercase.
    goodstorecode = models.IntegerField(db_column='GoodStoreCode', blank=True, null=True)  # Field name made lowercase.
    productstorecode = models.IntegerField(db_column='ProductStoreCode', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Toolid_Kala'


class ToolidKalacodeVar(models.Model):
    toolid_code = models.IntegerField(db_column='Toolid_Code', blank=True, null=True)  # Field name made lowercase.
    kala_code = models.IntegerField(db_column='Kala_Code', blank=True, null=True)  # Field name made lowercase.
    meghdar = models.DecimalField(db_column='Meghdar', max_digits=23, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    tmp = models.SmallIntegerField(blank=True, null=True)
    com_index = models.IntegerField(db_column='Com_Index')  # Field name made lowercase.
    radif = models.IntegerField(db_column='Radif', blank=True, null=True)  # Field name made lowercase.
    anbar = models.IntegerField(db_column='Anbar', blank=True, null=True)  # Field name made lowercase.
    meghdar2 = models.DecimalField(max_digits=23, decimal_places=8, blank=True, null=True)
    comment = models.CharField(db_column='Comment', max_length=500, blank=True, null=True)  # Field name made lowercase.
    cost = models.DecimalField(db_column='Cost', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    costpercent = models.DecimalField(db_column='CostPercent', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    costpercenttype = models.BooleanField(db_column='CostPercentType', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Toolid_KalaCode_Var'


class ToolidKalaDetail(models.Model):
    kala_code = models.IntegerField(db_column='Kala_Code', blank=True, null=True)  # Field name made lowercase.
    meghdar = models.DecimalField(db_column='Meghdar', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    status = models.SmallIntegerField(db_column='Status', blank=True, null=True)  # Field name made lowercase.
    toolid_code = models.SmallIntegerField(db_column='Toolid_Code', blank=True, null=True)  # Field name made lowercase.
    type = models.SmallIntegerField(db_column='Type', blank=True, null=True)  # Field name made lowercase.
    com_index = models.IntegerField(db_column='Com_Index')  # Field name made lowercase.
    rowid = models.AutoField(db_column='rowId',primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Toolid_Kala_Detail'


class ToolidVar(models.Model):
    code = models.IntegerField(db_column='Code', primary_key=True)  # Field name made lowercase. The composite primary key (Code, tmp) found, that is not supported. The first column is selected.
    date = models.CharField(db_column='Date', max_length=10, blank=True, null=True)  # Field name made lowercase.
    comment = models.CharField(db_column='Comment', max_length=500, blank=True, null=True)  # Field name made lowercase.
    mablagh = models.DecimalField(db_column='Mablagh', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    meghdar = models.DecimalField(db_column='Meghdar', max_digits=23, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    tmp = models.SmallIntegerField()
    com_index = models.IntegerField(db_column='Com_Index')  # Field name made lowercase.
    meghdar2 = models.DecimalField(max_digits=23, decimal_places=8, blank=True, null=True)
    vouchercode = models.IntegerField(db_column='VoucherCode', blank=True, null=True)  # Field name made lowercase.
    calctype = models.SmallIntegerField(db_column='CalcType', blank=True, null=True)  # Field name made lowercase.
    expcentercode = models.IntegerField(db_column='ExpCenterCode', blank=True, null=True)  # Field name made lowercase.
    global_field = models.ForeignKey(GlobalIds, on_delete=models.DO_NOTHING, db_column='Global_ID', blank=True, null=True)  # Field name made lowercase. Field renamed because it was a Python reserved word.

    class Meta:
        managed = False
        db_table = 'Toolid_Var'
        unique_together = (('code', 'tmp'),)


class TransactionAsset(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    obtaincode = models.IntegerField(db_column='ObtainCode')  # Field name made lowercase.
    date = models.CharField(db_column='Date', max_length=10)  # Field name made lowercase.
    code = models.IntegerField(db_column='Code')  # Field name made lowercase.
    type = models.SmallIntegerField(db_column='Type')  # Field name made lowercase.
    amount = models.IntegerField(db_column='Amount')  # Field name made lowercase.
    cost = models.DecimalField(db_column='Cost', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Transaction_Asset'


class Tshareholders(models.Model):
    percode = models.IntegerField(db_column='PerCode', blank=True, null=True)  # Field name made lowercase.
    precent = models.DecimalField(db_column='Precent', max_digits=23, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    comment = models.CharField(db_column='Comment', max_length=500, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Tshareholders'


class Units(models.Model):
    code = models.SmallIntegerField(db_column='Code', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=50, blank=True, null=True)  # Field name made lowercase.
    comment = models.CharField(db_column='Comment', max_length=500, blank=True, null=True)  # Field name made lowercase.
    type = models.SmallIntegerField(db_column='Type', blank=True, null=True)  # Field name made lowercase.
    unittin = models.CharField(db_column='UnitTIN', max_length=50, blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return self.name if self.name else f"واحد کد {self.code}"

    class Meta:
        managed = False
        db_table = 'Units'


class Unsenttable(models.Model):
    plu = models.IntegerField(db_column='PLU', primary_key=True)  # Field name made lowercase.
    scale1 = models.CharField(db_column='Scale1', max_length=10, blank=True, null=True)  # Field name made lowercase.
    scale2 = models.CharField(db_column='Scale2', max_length=10, blank=True, null=True)  # Field name made lowercase.
    scale3 = models.CharField(db_column='Scale3', max_length=10, blank=True, null=True)  # Field name made lowercase.
    scale4 = models.CharField(db_column='Scale4', max_length=10, blank=True, null=True)  # Field name made lowercase.
    scale5 = models.CharField(db_column='Scale5', max_length=10, blank=True, null=True)  # Field name made lowercase.
    scale6 = models.CharField(db_column='Scale6', max_length=10, blank=True, null=True)  # Field name made lowercase.
    scale7 = models.CharField(db_column='Scale7', max_length=10, blank=True, null=True)  # Field name made lowercase.
    scale8 = models.CharField(db_column='Scale8', max_length=10, blank=True, null=True)  # Field name made lowercase.
    scale9 = models.CharField(db_column='Scale9', max_length=10, blank=True, null=True)  # Field name made lowercase.
    scale10 = models.CharField(db_column='Scale10', max_length=10, blank=True, null=True)  # Field name made lowercase.
    scale11 = models.CharField(db_column='Scale11', max_length=10, blank=True, null=True)  # Field name made lowercase.
    scale12 = models.CharField(db_column='Scale12', max_length=10, blank=True, null=True)  # Field name made lowercase.
    scale13 = models.CharField(db_column='Scale13', max_length=10, blank=True, null=True)  # Field name made lowercase.
    scale14 = models.CharField(db_column='Scale14', max_length=10, blank=True, null=True)  # Field name made lowercase.
    scale15 = models.CharField(db_column='Scale15', max_length=10, blank=True, null=True)  # Field name made lowercase.
    scale16 = models.CharField(db_column='Scale16', max_length=10, blank=True, null=True)  # Field name made lowercase.
    scale17 = models.CharField(db_column='Scale17', max_length=10, blank=True, null=True)  # Field name made lowercase.
    scale18 = models.CharField(db_column='Scale18', max_length=10, blank=True, null=True)  # Field name made lowercase.
    scale19 = models.CharField(db_column='Scale19', max_length=10, blank=True, null=True)  # Field name made lowercase.
    scale20 = models.CharField(db_column='Scale20', max_length=10, blank=True, null=True)  # Field name made lowercase.
    scale21 = models.CharField(db_column='Scale21', max_length=10, blank=True, null=True)  # Field name made lowercase.
    scale22 = models.CharField(db_column='Scale22', max_length=10, blank=True, null=True)  # Field name made lowercase.
    scale23 = models.CharField(db_column='Scale23', max_length=10, blank=True, null=True)  # Field name made lowercase.
    scale24 = models.CharField(db_column='Scale24', max_length=10, blank=True, null=True)  # Field name made lowercase.
    scale25 = models.CharField(db_column='Scale25', max_length=10, blank=True, null=True)  # Field name made lowercase.
    scale26 = models.CharField(db_column='Scale26', max_length=10, blank=True, null=True)  # Field name made lowercase.
    scale27 = models.CharField(db_column='Scale27', max_length=10, blank=True, null=True)  # Field name made lowercase.
    scale28 = models.CharField(db_column='Scale28', max_length=10, blank=True, null=True)  # Field name made lowercase.
    scale29 = models.CharField(db_column='Scale29', max_length=10, blank=True, null=True)  # Field name made lowercase.
    scale30 = models.CharField(db_column='Scale30', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'UnsentTable'


class Userevent(models.Model):
    userid = models.ForeignKey('Users', on_delete=models.DO_NOTHING, db_column='UserID')  # Field name made lowercase.
    partpermissionid = models.ForeignKey(Partpermission, on_delete=models.DO_NOTHING, db_column='PartPermissionID')  # Field name made lowercase.
    success = models.BooleanField(db_column='Success')  # Field name made lowercase.
    date = models.CharField(db_column='Date', max_length=10, blank=True, null=True)  # Field name made lowercase.
    time = models.CharField(db_column='Time', max_length=5, blank=True, null=True)  # Field name made lowercase.
    comment = models.CharField(db_column='Comment', max_length=500, blank=True, null=True)  # Field name made lowercase.
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'UserEvent'


class Userlog(models.Model):
    userid = models.ForeignKey('Users', on_delete=models.DO_NOTHING, db_column='UserID')  # Field name made lowercase.
    computerid = models.SmallIntegerField(db_column='ComputerID', blank=True, null=True)  # Field name made lowercase.
    startdate = models.CharField(db_column='StartDate', max_length=10, blank=True, null=True)  # Field name made lowercase.
    enddate = models.CharField(db_column='EndDate', max_length=10, blank=True, null=True)  # Field name made lowercase.
    starttime = models.CharField(db_column='StartTime', max_length=5, blank=True, null=True)  # Field name made lowercase.
    endtime = models.CharField(db_column='EndTime', max_length=5, blank=True, null=True)  # Field name made lowercase.
    active = models.SmallIntegerField(db_column='Active', blank=True, null=True)  # Field name made lowercase.
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'UserLog'


class Userpermission(models.Model):
    userid = models.ForeignKey('Users', on_delete=models.DO_NOTHING, db_column='UserID')  # Field name made lowercase.
    partpermissionid = models.ForeignKey(Partpermission, on_delete=models.DO_NOTHING, db_column='PartPermissionID')  # Field name made lowercase.
    permission = models.BooleanField(db_column='Permission', blank=True, null=True)  # Field name made lowercase.
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'UserPermission'
        unique_together = (('userid', 'partpermissionid'),)


class Userquestions(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    questioncode = models.ForeignKey(Questions, on_delete=models.DO_NOTHING, db_column='QuestionCode', blank=True, null=True)  # Field name made lowercase.
    question = models.CharField(db_column='Question', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    offer = models.CharField(db_column='Offer', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    flag = models.SmallIntegerField(db_column='Flag', blank=True, null=True)  # Field name made lowercase.
    creatdate = models.DateTimeField(db_column='CreatDate', blank=True, null=True)  # Field name made lowercase.
    ansdate = models.DateTimeField(db_column='AnsDate', blank=True, null=True)  # Field name made lowercase.
    subject = models.CharField(max_length=100, blank=True, null=True)
    trackcode = models.CharField(db_column='TrackCode', max_length=20, blank=True, null=True)  # Field name made lowercase.
    mem = models.CharField(max_length=4000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'UserQuestions'


class Uservalidityquestions(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    questioncode = models.ForeignKey(Questions, on_delete=models.DO_NOTHING, db_column='QuestionCode')  # Field name made lowercase.
    question = models.CharField(db_column='Question', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    date = models.CharField(db_column='Date', max_length=30)  # Field name made lowercase.
    flag = models.BooleanField(db_column='Flag', blank=True, null=True)  # Field name made lowercase.
    grace = models.BooleanField(db_column='Grace', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'UserValidityQuestions'


class Users(models.Model):
    name = models.CharField(db_column='Name', max_length=50)  # Field name made lowercase.
    code = models.IntegerField(db_column='Code')  # Field name made lowercase.
    semat = models.SmallIntegerField(db_column='Semat')  # Field name made lowercase.
    pass_field = models.CharField(db_column='Pass', max_length=250, blank=True, null=True)  # Field name made lowercase. Field renamed because it was a Python reserved word.
    pic = models.CharField(db_column='Pic', max_length=255, blank=True, null=True)  # Field name made lowercase.
    status = models.SmallIntegerField(db_column='Status', db_comment='0=active; 1=inactive;')  # Field name made lowercase.
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    managetype = models.SmallIntegerField(db_column='ManageType')  # Field name made lowercase.
    picture = models.BinaryField(db_column='Picture', blank=True, null=True)  # Field name made lowercase.
    admintype = models.SmallIntegerField(db_column='AdminType', blank=True, null=True)  # Field name made lowercase.
    srl_opratorgroup = models.IntegerField(db_column='Srl_OpratorGroup', blank=True, null=True)  # Field name made lowercase.
    is_active = models.BooleanField(db_column='Is_Active')  # Field name made lowercase.
    telline = models.CharField(db_column='TelLine', max_length=15)  # Field name made lowercase.
    orderinlist = models.IntegerField(db_column='OrderInList')  # Field name made lowercase.
    mobile = models.CharField(db_column='Mobile', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Users'


class Usersdesktopitems(models.Model):
    id =  models.AutoField(db_column='ID', primary_key=True)# Field name made lowercase.
    itemcode = models.IntegerField(db_column='ItemCode', blank=True, null=True)  # Field name made lowercase.
    userid = models.IntegerField(db_column='UserID', blank=True, null=True)  # Field name made lowercase.
    displayorder = models.IntegerField(db_column='DisplayOrder', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'UsersDesktopItems'


class Vendors(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    code = models.IntegerField(db_column='Code')  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=26, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Vendors'


class VoiceSendState(models.Model):
    id_voice_message = models.ForeignKey('VoiceSendMessages', on_delete=models.DO_NOTHING, db_column='id_voice_message', blank=True, null=True)
    idmessage = models.CharField(max_length=50, blank=True, null=True)
    number = models.CharField(max_length=50, blank=True, null=True)
    state = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Voice_Send_state'


class WarehousehandlingDetail(models.Model):
    whhcode = models.IntegerField(db_column='WHHCode', primary_key=True)  # Field name made lowercase. The composite primary key (WHHCode, tmp) found, that is not supported. The first column is selected.
    rowno = models.IntegerField(db_column='RowNo')  # Field name made lowercase.
    goodcode = models.ForeignKey(Goodinf, on_delete=models.DO_NOTHING, db_column='GoodCode')  # Field name made lowercase.
    storecode = models.IntegerField(db_column='StoreCode', blank=True, null=True)  # Field name made lowercase.
    grpcode = models.IntegerField(db_column='GrpCode', blank=True, null=True)  # Field name made lowercase.
    goodname = models.CharField(db_column='GoodName', max_length=500, blank=True, null=True)  # Field name made lowercase.
    storename = models.CharField(db_column='StoreName', max_length=500, blank=True, null=True)  # Field name made lowercase.
    goodunit = models.CharField(db_column='GoodUnit', max_length=50, blank=True, null=True)  # Field name made lowercase.
    realcount = models.DecimalField(db_column='RealCount', max_digits=23, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    firstcount = models.DecimalField(db_column='FirstCount', max_digits=23, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    secondcount = models.DecimalField(db_column='SecondCount', max_digits=23, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    thirdcount = models.DecimalField(db_column='ThirdCount', max_digits=23, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    checkamount = models.SmallIntegerField(db_column='CheckAmount', blank=True, null=True)  # Field name made lowercase.
    abbname = models.CharField(db_column='AbbName', max_length=300, blank=True, null=True)  # Field name made lowercase.
    tmp = models.SmallIntegerField()
    whcoderef = models.IntegerField(db_column='WHCodeRef', blank=True, null=True)  # Field name made lowercase.
    mogodicount = models.DecimalField(db_column='MogodiCount', max_digits=23, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    cost = models.DecimalField(db_column='Cost', max_digits=23, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=250, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WareHouseHandling_Detail'
        unique_together = (('whhcode', 'tmp'),)


class WarehousehandlingInfo(models.Model):
    whdate = models.CharField(db_column='WHDate', max_length=10, blank=True, null=True)  # Field name made lowercase.
    adjustmenttype = models.SmallIntegerField(db_column='AdjustmentType', blank=True, null=True)  # Field name made lowercase.
    issaved = models.BooleanField(db_column='IsSaved', blank=True, null=True)  # Field name made lowercase.
    inc_acctype = models.SmallIntegerField(db_column='Inc_AccType', blank=True, null=True)  # Field name made lowercase.
    inc_total = models.IntegerField(db_column='Inc_Total', blank=True, null=True)  # Field name made lowercase.
    inc_assistant = models.IntegerField(db_column='Inc_Assistant', blank=True, null=True)  # Field name made lowercase.
    inc_detail = models.IntegerField(db_column='Inc_Detail', blank=True, null=True)  # Field name made lowercase.
    inc_expensecenter = models.IntegerField(db_column='Inc_ExpenseCenter', blank=True, null=True)  # Field name made lowercase.
    exp_acctype = models.SmallIntegerField(db_column='Exp_AccType', blank=True, null=True)  # Field name made lowercase.
    exp_total = models.IntegerField(db_column='Exp_Total', blank=True, null=True)  # Field name made lowercase.
    exp_assistant = models.IntegerField(db_column='Exp_Assistant', blank=True, null=True)  # Field name made lowercase.
    exp_detail = models.IntegerField(db_column='Exp_Detail', blank=True, null=True)  # Field name made lowercase.
    exp_expensecenter = models.IntegerField(db_column='Exp_ExpenseCenter', blank=True, null=True)  # Field name made lowercase.
    whcode = models.IntegerField(db_column='WHCode', primary_key=True)  # Field name made lowercase. The composite primary key (WHCode, tmp) found, that is not supported. The first column is selected.
    tmp = models.SmallIntegerField()
    whname = models.CharField(db_column='WHName', max_length=250)  # Field name made lowercase.
    responsiblecoderef = models.IntegerField(db_column='ResponsibleCodeRef')  # Field name made lowercase.
    storescoderef = models.ForeignKey(Stores, on_delete=models.DO_NOTHING, db_column='StoresCodeRef')  # Field name made lowercase.
    status = models.SmallIntegerField(db_column='Status')  # Field name made lowercase.
    desnumerationfirst = models.CharField(db_column='DesNumerationFirst', max_length=250, blank=True, null=True)  # Field name made lowercase.
    desnumerationsecond = models.CharField(db_column='DesNumerationSecond', max_length=250, blank=True, null=True)  # Field name made lowercase.
    com_index = models.IntegerField(db_column='Com_Index', blank=True, null=True)  # Field name made lowercase.
    global_id = models.IntegerField(db_column='Global_ID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WareHouseHandling_Info'
        unique_together = (('whcode', 'tmp'),)


class WorktimeMap(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=100, blank=True, null=True)  # Field name made lowercase.
    comment = models.CharField(db_column='Comment', max_length=400, blank=True, null=True)  # Field name made lowercase.
    default = models.BooleanField(db_column='Default', blank=True, null=True)  # Field name made lowercase.
    worktime = models.CharField(db_column='WorkTime', max_length=100, blank=True, null=True)  # Field name made lowercase.
    percode = models.CharField(db_column='PerCode', max_length=100, blank=True, null=True)  # Field name made lowercase.
    fromdate = models.CharField(db_column='FromDate', max_length=100, blank=True, null=True)  # Field name made lowercase.
    todate = models.CharField(db_column='ToDate', max_length=100, blank=True, null=True)  # Field name made lowercase.
    readdatefromexcel = models.SmallIntegerField(db_column='ReadDateFromExcel')  # Field name made lowercase.
    excelfile = models.CharField(db_column='ExcelFile', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WorkTime_Map'


class WorktimeMapdetail(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    mapcode = models.IntegerField(db_column='MapCode', blank=True, null=True)  # Field name made lowercase.
    item_type = models.BooleanField(db_column='Item_Type', blank=True, null=True)  # Field name made lowercase.
    item_code = models.IntegerField(db_column='Item_Code', blank=True, null=True)  # Field name made lowercase.
    column_name = models.CharField(db_column='Column_Name', max_length=250, blank=True, null=True)  # Field name made lowercase.
    comment = models.CharField(db_column='Comment', max_length=500, blank=True, null=True)  # Field name made lowercase.
    column_type = models.SmallIntegerField(db_column='Column_Type', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WorkTime_MapDetail'


class WorktimeMapexcelfield(models.Model):
    idcolumnexcel = models.AutoField(db_column='idColumnExcel', primary_key=True)  # Field name made lowercase.
    mapcode = models.IntegerField(db_column='MapCode')  # Field name made lowercase.
    column_nameexcel = models.CharField(db_column='Column_NameExcel', max_length=250)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WorkTime_MapExcelField'


class Yearclose(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=200, blank=True, null=True)  # Field name made lowercase.
    sharh = models.CharField(db_column='Sharh', max_length=200, blank=True, null=True)  # Field name made lowercase.
    bench_script = models.TextField(db_column='Bench_Script', blank=True, null=True)  # Field name made lowercase.
    checking_mode = models.SmallIntegerField(db_column='Checking_Mode', blank=True, null=True)  # Field name made lowercase.
    condition = models.IntegerField(db_column='Condition', blank=True, null=True)  # Field name made lowercase.
    target = models.SmallIntegerField(db_column='Target', blank=True, null=True)  # Field name made lowercase.
    specialtype = models.IntegerField(db_column='SpecialType', blank=True, null=True)  # Field name made lowercase.
    userguide = models.CharField(db_column='UserGuide', max_length=2000, blank=True, null=True)  # Field name made lowercase.
    attention = models.CharField(db_column='Attention', max_length=1500, blank=True, null=True)  # Field name made lowercase.
    solve_script = models.CharField(db_column='Solve_Script', max_length=1500, blank=True, null=True)  # Field name made lowercase.
    settings = models.CharField(db_column='Settings', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    resultstatus = models.SmallIntegerField(db_column='ResultStatus', blank=True, null=True)  # Field name made lowercase.
    priority = models.IntegerField(db_column='Priority')  # Field name made lowercase.
    code = models.IntegerField(db_column='Code')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'YearClose'


class Yearclosedetail(models.Model):
    idyearclose = models.IntegerField(db_column='IDYearClose', blank=True, null=True)  # Field name made lowercase.
    idfiscalyear = models.IntegerField(db_column='IDFiscalYear', blank=True, null=True)  # Field name made lowercase.
    date = models.CharField(db_column='Date', max_length=10, blank=True, null=True)  # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=500, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'YearCloseDetail'


class Yearsood(models.Model):
    yearcode = models.IntegerField(db_column='YearCode', blank=True, null=True)  # Field name made lowercase.
    sood = models.DecimalField(db_column='Sood', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'YearSood'


class Zone(models.Model):
    shahrcode = models.IntegerField(db_column='ShahrCode', blank=True, null=True)  # Field name made lowercase.
    shahr = models.CharField(db_column='Shahr', max_length=100, blank=True, null=True)  # Field name made lowercase.
    ostan = models.CharField(db_column='Ostan', max_length=100, blank=True, null=True)  # Field name made lowercase.
    ostancode = models.IntegerField(db_column='OstanCode', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Zone'


class BackfactVisitor(models.Model):
    id = id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    backfact_code = models.IntegerField(db_column='BackFact_code', blank=True, null=True)  # Field name made lowercase.
    per_code = models.IntegerField(db_column='Per_code', blank=True, null=True)  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=50, blank=True, null=True)  # Field name made lowercase.
    percent = models.DecimalField(db_column='Percent', max_digits=23, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    price = models.DecimalField(db_column='Price', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    tmp = models.BooleanField(blank=True, null=True)
    type_pay = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'backFact_Visitor'


class Bb0(models.Model):
    id =  models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    id_check = models.CharField(db_column='ID_Check', max_length=50)  # Field name made lowercase.
    radif_check = models.IntegerField(db_column='Radif_Check', blank=True, null=True)  # Field name made lowercase.
    date2 = models.CharField(db_column='Date2', max_length=10, blank=True, null=True)  # Field name made lowercase.
    date1 = models.CharField(db_column='Date1', max_length=10)  # Field name made lowercase.
    amount = models.DecimalField(db_column='Amount', max_digits=23, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    bank = models.CharField(db_column='Bank', max_length=50, blank=True, null=True)  # Field name made lowercase.
    shobe = models.CharField(db_column='Shobe', max_length=50, blank=True, null=True)  # Field name made lowercase.
    id_h = models.CharField(db_column='ID_H', max_length=50, blank=True, null=True)  # Field name made lowercase.
    comment = models.CharField(db_column='Comment', max_length=500, blank=True, null=True)  # Field name made lowercase.
    status = models.IntegerField(db_column='Status', blank=True, null=True)  # Field name made lowercase.
    perid = models.IntegerField(db_column='PerID')  # Field name made lowercase.
    first1 = models.SmallIntegerField(db_column='First1')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'bb0'


class Bb1(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    id_check = models.CharField(db_column='ID_Check', max_length=50)  # Field name made lowercase.
    radif_check = models.IntegerField(db_column='Radif_Check', blank=True, null=True)  # Field name made lowercase.
    date2 = models.CharField(db_column='Date2', max_length=10, blank=True, null=True)  # Field name made lowercase.
    date1 = models.CharField(db_column='Date1', max_length=10)  # Field name made lowercase.
    amount = models.DecimalField(db_column='Amount', max_digits=23, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    id_bank = models.IntegerField(db_column='ID_Bank', blank=True, null=True)  # Field name made lowercase.
    comment = models.CharField(db_column='Comment', max_length=500, blank=True, null=True)  # Field name made lowercase.
    status = models.IntegerField(db_column='Status', blank=True, null=True)  # Field name made lowercase.
    first1 = models.SmallIntegerField(db_column='First1')  # Field name made lowercase.
    chequecounter = models.IntegerField(db_column='ChequeCounter')  # Field name made lowercase.
    perid = models.IntegerField(db_column='PerID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'bb1'


class Bb2(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)   # Field name made lowercase.
    date1 = models.CharField(db_column='Date1', max_length=10)  # Field name made lowercase.
    id_check = models.CharField(db_column='ID_Check', max_length=50)  # Field name made lowercase.
    amount = models.DecimalField(db_column='Amount', max_digits=23, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    comment = models.CharField(db_column='Comment', max_length=500, blank=True, null=True)  # Field name made lowercase.
    id_bank = models.IntegerField(db_column='Id_Bank', blank=True, null=True)  # Field name made lowercase.
    sanad_code = models.IntegerField(db_column='Sanad_Code')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'bb2'


class Bb4(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)   # Field name made lowercase.
    date1 = models.CharField(db_column='Date1', max_length=10)  # Field name made lowercase.
    id_check = models.CharField(db_column='ID_CHeck', max_length=50)  # Field name made lowercase.
    amount = models.DecimalField(db_column='Amount', max_digits=23, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    comment = models.CharField(db_column='Comment', max_length=500, blank=True, null=True)  # Field name made lowercase.
    id_bank = models.IntegerField(db_column='Id_Bank', blank=True, null=True)  # Field name made lowercase.
    typ = models.IntegerField(db_column='Typ', blank=True, null=True)  # Field name made lowercase.
    bank = models.CharField(db_column='Bank', max_length=50, blank=True, null=True)  # Field name made lowercase.
    shobe = models.CharField(db_column='Shobe', max_length=50, blank=True, null=True)  # Field name made lowercase.
    id_h = models.CharField(db_column='ID_H', max_length=50, blank=True, null=True)  # Field name made lowercase.
    rec = models.IntegerField(db_column='Rec')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'bb4'


class CategoryGallery(models.Model):
    id = models.IntegerField(db_column='Id', primary_key=True)  # Field name made lowercase.
    parentid = models.IntegerField(db_column='ParentId', blank=True, null=True)  # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'category_gallery'


class Colors(models.Model):
    code = models.AutoField(primary_key=True)
    h_img = models.BinaryField(db_column='H-img')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    l_img = models.BinaryField(db_column='l-img')  # Field renamed to remove unsuitable characters.
    cl_code = models.CharField(max_length=9, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'colors'


class Dtproperties(models.Model):
    objectid = models.IntegerField(blank=True, null=True)
    property = models.CharField(max_length=64)
    value = models.CharField(max_length=255, blank=True, null=True)
    uvalue = models.CharField(max_length=255, blank=True, null=True)
    lvalue = models.BinaryField(blank=True, null=True)
    version = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'dtproperties'
        unique_together = (('id', 'property'),)


class InfCo(models.Model):
    name_co = models.CharField(max_length=50)
    ymali = models.CharField(max_length=20, blank=True, null=True)
    tel = models.CharField(max_length=120, blank=True, null=True)
    tel2 = models.CharField(max_length=11, blank=True, null=True)
    addr = models.CharField(max_length=200, blank=True, null=True)
    logo = models.CharField(db_column='Logo', max_length=200, blank=True, null=True)  # Field name made lowercase.
    date = models.CharField(db_column='Date', max_length=10, blank=True, null=True)  # Field name made lowercase.
    economicno = models.CharField(db_column='EconomicNo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    regno = models.CharField(db_column='RegNo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    postcode_high = models.CharField(db_column='PostCode_High', max_length=5, blank=True, null=True)  # Field name made lowercase.
    postcode_low = models.CharField(db_column='PostCode_Low', max_length=5, blank=True, null=True)  # Field name made lowercase.
    jobdescription = models.CharField(db_column='JobDescription', max_length=200, blank=True, null=True)  # Field name made lowercase.
    logodata = models.BinaryField(db_column='LogoData', blank=True, null=True)  # Field name made lowercase.
    closeddate = models.CharField(db_column='ClosedDate', max_length=10, blank=True, null=True)  # Field name made lowercase.
    sh_meli = models.CharField(db_column='SH_meli', max_length=15, blank=True, null=True)  # Field name made lowercase.
    dateend = models.CharField(db_column='DateEnd', max_length=10, blank=True, null=True)  # Field name made lowercase.
    statusalarmfiscal = models.SmallIntegerField(db_column='StatusAlarmFiscal', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'inf_co'


class KharidDetail(models.Model):
    code = models.OneToOneField(Kharid, on_delete=models.DO_NOTHING, db_column='code', primary_key=True)  # The composite primary key (code, radif) found, that is not supported. The first column is selected.
    radif = models.SmallIntegerField()
    an_code = models.SmallIntegerField(blank=True, null=True)
    kala_code = models.IntegerField()
    sharh = models.CharField(max_length=500, blank=True, null=True)
    meghdar = models.DecimalField(max_digits=23, decimal_places=8, blank=True, null=True)
    naghdi = models.DecimalField(max_digits=23, decimal_places=9, blank=True, null=True)
    reval = models.IntegerField(blank=True, null=True)
    haml = models.DecimalField(max_digits=23, decimal_places=9, blank=True, null=True)
    sh_mashin = models.CharField(max_length=50, blank=True, null=True)
    sh_barnameh = models.CharField(max_length=50, blank=True, null=True)
    code_driver = models.IntegerField(blank=True, null=True)
    status = models.SmallIntegerField(db_column='Status', blank=True, null=True)  # Field name made lowercase.
    vaziyat = models.SmallIntegerField()
    type = models.SmallIntegerField(db_column='Type', blank=True, null=True)  # Field name made lowercase.
    tool = models.DecimalField(max_digits=23, decimal_places=8, blank=True, null=True)
    arz = models.DecimalField(max_digits=23, decimal_places=8, blank=True, null=True)
    tedad = models.IntegerField(blank=True, null=True)
    meghdar2 = models.DecimalField(max_digits=23, decimal_places=8, blank=True, null=True)
    bestype = models.SmallIntegerField(db_column='BesType', blank=True, null=True)  # Field name made lowercase.
    bedtype = models.SmallIntegerField(db_column='BedType', blank=True, null=True)  # Field name made lowercase.
    com_index = models.IntegerField()
    chargepercent = models.DecimalField(db_column='ChargePercent', max_digits=23, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    taxpercent = models.DecimalField(db_column='TaxPercent', max_digits=23, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    hazinecomment = models.CharField(db_column='HazineComment', max_length=500, blank=True, null=True)  # Field name made lowercase.
    hazinecode = models.IntegerField(db_column='HazineCode', blank=True, null=True)  # Field name made lowercase.
    takhfif = models.DecimalField(max_digits=23, decimal_places=9, blank=True, null=True)
    takhfif_type = models.BooleanField(db_column='Takhfif_Type', blank=True, null=True)  # Field name made lowercase.
    off_user = models.DecimalField(db_column='Off_User', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    off_sys = models.DecimalField(db_column='Off_Sys', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    cost_entery_type = models.BooleanField(db_column='Cost_Entery_Type', blank=True, null=True)  # Field name made lowercase.
    totalcost = models.DecimalField(db_column='TotalCost', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    currcode = models.IntegerField(db_column='CurrCode', blank=True, null=True)  # Field name made lowercase.
    currrate = models.DecimalField(db_column='CurrRate', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    takhfif_costtype = models.BooleanField(db_column='Takhfif_CostType', blank=True, null=True)  # Field name made lowercase.
    ordercode = models.IntegerField(db_column='OrderCode', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'kharid_detail'
        unique_together = (('code', 'radif'),)


class PerfactVisitor(models.Model):
    id = id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    fact_code = models.IntegerField(blank=True, null=True)
    per_code = models.IntegerField(db_column='Per_code', blank=True, null=True)  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=50, blank=True, null=True)  # Field name made lowercase.
    percent = models.DecimalField(db_column='Percent', max_digits=23, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    price = models.DecimalField(db_column='Price', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    tmp = models.BooleanField(blank=True, null=True)
    type_pay = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'perFact_Visitor'


class PicStore(models.Model):
    pic_add = models.CharField(max_length=100, blank=True, null=True)
    code = models.IntegerField(blank=True, null=True)
    type = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pic_store'


class Rooznameh(models.Model):
    code = models.IntegerField(primary_key=True)  # The composite primary key (code, radif) found, that is not supported. The first column is selected.
    radif = models.IntegerField()
    kol = models.SmallIntegerField(blank=True, null=True)
    moin = models.SmallIntegerField(blank=True, null=True)
    tafzili = models.SmallIntegerField(blank=True, null=True)
    sharh = models.CharField(max_length=500, blank=True, null=True)
    status = models.SmallIntegerField(blank=True, null=True)
    bed = models.DecimalField(max_digits=23, decimal_places=9, blank=True, null=True)
    bes = models.DecimalField(max_digits=23, decimal_places=9, blank=True, null=True)
    sanad_code = models.CharField(db_column='Sanad_Code', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sanad_type = models.IntegerField(db_column='Sanad_Type', blank=True, null=True)  # Field name made lowercase.
    tarikh = models.CharField(db_column='Tarikh', max_length=10, blank=True, null=True)  # Field name made lowercase.
    meghdar = models.DecimalField(db_column='Meghdar', max_digits=23, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    com_index = models.IntegerField(db_column='Com_Index')  # Field name made lowercase.
    zamaem = models.IntegerField(db_column='Zamaem', blank=True, null=True)  # Field name made lowercase.
    store = models.SmallIntegerField(db_column='Store', blank=True, null=True)  # Field name made lowercase.
    sanadid = models.IntegerField(db_column='SanadID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'rooznameh'
        unique_together = (('code', 'radif'),)


class RsPersonMoreinfo(models.Model):
    person_id = models.IntegerField(db_column='Person_ID', blank=True, null=True)  # Field name made lowercase.
    flag = models.IntegerField(db_column='Flag', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'rs_Person_MoreInfo'


class RsSerial(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    parent = models.ForeignKey(RsTechnisionComponents, on_delete=models.DO_NOTHING, db_column='Parent_ID')  # Field name made lowercase.
    serial = models.CharField(db_column='Serial', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'rs_Serial'


class RsGuarantee(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=100, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=500, blank=True, null=True)  # Field name made lowercase.
    tel = models.CharField(db_column='Tel', max_length=50, blank=True, null=True)  # Field name made lowercase.
    mobile = models.CharField(db_column='Mobile', max_length=50, blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=300, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'rs_guarantee'


class RsMessage(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=100)  # Field name made lowercase.
    message = models.CharField(db_column='Message', max_length=1000)  # Field name made lowercase.
    desc = models.CharField(db_column='Desc', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    type = models.SmallIntegerField(db_column='Type')  # Field name made lowercase.
    button_1 = models.CharField(db_column='Button_1', max_length=100, blank=True, null=True)  # Field name made lowercase.
    button_2 = models.CharField(db_column='Button_2', max_length=100, blank=True, null=True)  # Field name made lowercase.
    button_3 = models.CharField(db_column='Button_3', max_length=100, blank=True, null=True)  # Field name made lowercase.
    button_4 = models.CharField(db_column='Button_4', max_length=100, blank=True, null=True)  # Field name made lowercase.
    default_btn = models.SmallIntegerField(db_column='Default_BTN')  # Field name made lowercase.
    cancel_btn = models.SmallIntegerField(db_column='Cancel_BTN')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'rs_message'


class RsMessageDetail(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    msg_id = models.IntegerField(db_column='MSG_ID')  # Field name made lowercase.
    partcode = models.IntegerField(db_column='PartCode')  # Field name made lowercase.
    remember = models.SmallIntegerField(db_column='Remember')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'rs_message_detail'


class RsMobileSendsms(models.Model):
    mobile = models.CharField(db_column='Mobile', max_length=20, blank=True, null=True)  # Field name made lowercase.
    sms = models.CharField(db_column='SMS', max_length=1000, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'rs_mobile_sendsms'


class RsMobileSendsms1(models.Model):
    mobile = models.CharField(db_column='Mobile', max_length=20, blank=True, null=True)  # Field name made lowercase.
    sms = models.CharField(db_column='SMS', max_length=1000, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'rs_mobile_sendsms_1'


class RsSell(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    customer_id = models.IntegerField(db_column='Customer_ID', blank=True, null=True)  # Field name made lowercase.
    number = models.CharField(db_column='Number', max_length=10, blank=True, null=True)  # Field name made lowercase.
    discount = models.DecimalField(db_column='Discount', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    date = models.CharField(db_column='Date', max_length=10, blank=True, null=True)  # Field name made lowercase.
    comment = models.CharField(db_column='Comment', max_length=500, blank=True, null=True)  # Field name made lowercase.
    details_cost = models.DecimalField(db_column='Details_Cost', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    details_discount = models.DecimalField(db_column='Details_Discount', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    charge_cost = models.DecimalField(db_column='Charge_Cost', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tax_cost = models.DecimalField(db_column='Tax_Cost', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    flag = models.SmallIntegerField(db_column='Flag', blank=True, null=True)  # Field name made lowercase.
    transport_cost = models.DecimalField(db_column='Transport_Cost', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    transport_personid = models.IntegerField(db_column='Transport_PersonID', blank=True, null=True)  # Field name made lowercase.
    transport_bycustomer = models.BooleanField(db_column='Transport_ByCustomer', blank=True, null=True)  # Field name made lowercase.
    invoice_code = models.IntegerField(db_column='Invoice_Code', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'rs_sell'


class RsServiceGuarantee(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    enterance_id = models.IntegerField(db_column='Enterance_ID')  # Field name made lowercase.
    send_date = models.CharField(db_column='Send_Date', max_length=10, blank=True, null=True)  # Field name made lowercase.
    guarantee_id = models.IntegerField(db_column='Guarantee_ID', blank=True, null=True)  # Field name made lowercase.
    status = models.SmallIntegerField(db_column='Status')  # Field name made lowercase.
    send_comment = models.CharField(db_column='Send_Comment', max_length=500, blank=True, null=True)  # Field name made lowercase.
    send_transport_cost = models.DecimalField(db_column='Send_Transport_Cost', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    send_transporterid = models.IntegerField(db_column='Send_TransporterID', blank=True, null=True)  # Field name made lowercase.
    send_transport_bycustomer = models.BooleanField(db_column='Send_Transport_ByCustomer', blank=True, null=True)  # Field name made lowercase.
    device_component = models.BooleanField(db_column='Device_Component', blank=True, null=True)  # Field name made lowercase.
    component_type = models.CharField(db_column='Component_Type', max_length=50, blank=True, null=True)  # Field name made lowercase.
    component_brand = models.CharField(db_column='Component_Brand', max_length=50, blank=True, null=True)  # Field name made lowercase.
    component_model = models.CharField(db_column='Component_Model', max_length=50, blank=True, null=True)  # Field name made lowercase.
    component_serial = models.CharField(db_column='Component_Serial', max_length=50, blank=True, null=True)  # Field name made lowercase.
    return_date = models.CharField(db_column='Return_Date', max_length=10, blank=True, null=True)  # Field name made lowercase.
    return_comment = models.CharField(db_column='Return_Comment', max_length=500, blank=True, null=True)  # Field name made lowercase.
    return_transport_cost = models.DecimalField(db_column='Return_Transport_Cost', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    return_transporterid = models.IntegerField(db_column='Return_TransporterID', blank=True, null=True)  # Field name made lowercase.
    return_transport_bycustomer = models.BooleanField(db_column='Return_Transport_ByCustomer', blank=True, null=True)  # Field name made lowercase.
    guarantee_cost = models.DecimalField(db_column='Guarantee_Cost', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    prev_state = models.SmallIntegerField(db_column='Prev_State')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'rs_service_guarantee'


class RsServiceServices(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    service_id = models.IntegerField(db_column='Service_ID')  # Field name made lowercase.
    serviceitem_id = models.IntegerField(db_column='ServiceItem_ID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'rs_service_services'


class RsTmpids(models.Model):
    id = models.IntegerField(db_column='ID', blank=True, primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'rs_tmpIDs'


class Schedule(models.Model):
    keyfield = models.AutoField(primary_key=True)
    date = models.CharField(max_length=10, blank=True, null=True)
    title = models.CharField(max_length=250, blank=True, null=True)
    person = models.CharField(max_length=250, blank=True, null=True)
    comment = models.CharField(max_length=5000, blank=True, null=True)
    status = models.SmallIntegerField(blank=True, null=True)
    alarm = models.SmallIntegerField(blank=True, null=True)
    r_date = models.CharField(db_column='R_date', max_length=10, blank=True, null=True)  # Field name made lowercase.
    codeperson = models.IntegerField(db_column='CodePerson', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'schedule'


class Sood(models.Model):
    code = models.IntegerField(blank=True, null=True)
    tarikh = models.CharField(max_length=10, blank=True, null=True)
    name = models.CharField(max_length=153, blank=True, null=True)
    sharh = models.CharField(max_length=500, blank=True, null=True)
    khales = models.DecimalField(max_digits=23, decimal_places=9, blank=True, null=True)
    sood = models.DecimalField(max_digits=23, decimal_places=9, blank=True, null=True)
    meghdar = models.DecimalField(max_digits=23, decimal_places=9, blank=True, null=True)
    naghdi = models.DecimalField(max_digits=23, decimal_places=9, blank=True, null=True)
    miangin = models.DecimalField(max_digits=23, decimal_places=9, blank=True, null=True)
    soodjoz = models.DecimalField(max_digits=23, decimal_places=9, blank=True, null=True)
    fcount = models.IntegerField(blank=True, null=True)
    percode = models.IntegerField(blank=True, null=True)
    kalagrpcode = models.IntegerField(db_column='KalaGrpCode', blank=True, null=True)  # Field name made lowercase.
    kalagrpname = models.CharField(db_column='KalaGrpName', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'sood'


class Soodforoosh(models.Model):
    radif = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=153, blank=True, null=True)
    meghdar = models.DecimalField(max_digits=23, decimal_places=9, blank=True, null=True)
    gheymat_miangin = models.DecimalField(max_digits=23, decimal_places=9, blank=True, null=True)
    naghdi = models.DecimalField(max_digits=23, decimal_places=9, blank=True, null=True)
    soodvahed = models.DecimalField(max_digits=23, decimal_places=9, blank=True, null=True)
    soodtedad = models.DecimalField(max_digits=23, decimal_places=9, blank=True, null=True)
    factcode = models.IntegerField(db_column='FactCode', blank=True, null=True)  # Field name made lowercase.
    percentsoodgood = models.FloatField(db_column='PercentSoodGood', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'soodforoosh'


class TerazAll(models.Model):
    radif = radif = models.AutoField(primary_key=True)
    kol = models.IntegerField(blank=True, null=True)
    moin = models.IntegerField(blank=True, null=True)
    code = models.CharField(max_length=50, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    mbed = models.DecimalField(max_digits=23, decimal_places=9, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'teraz_all'


class Tmpassignmentdetail(models.Model):
    code = models.IntegerField(db_column='Code', primary_key=True)  # Field name made lowercase. The composite primary key (Code, AssignmentCode) found, that is not supported. The first column is selected.
    assignmentcode = models.IntegerField(db_column='AssignmentCode')  # Field name made lowercase.
    goodcode = models.IntegerField(db_column='GoodCode', blank=True, null=True)  # Field name made lowercase.
    amount = models.DecimalField(db_column='Amount', max_digits=23, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    amount2 = models.DecimalField(db_column='Amount2', max_digits=23, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    cost = models.DecimalField(db_column='Cost', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    storecode = models.IntegerField(db_column='StoreCode', blank=True, null=True)  # Field name made lowercase.
    comment = models.CharField(db_column='Comment', max_length=500, blank=True, null=True)  # Field name made lowercase.
    width = models.DecimalField(db_column='Width', max_digits=23, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    height = models.DecimalField(db_column='Height', max_digits=23, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    num = models.DecimalField(db_column='Num', max_digits=23, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    global_id = models.IntegerField(db_column='Global_ID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tmpAssignmentDetail'
        unique_together = (('code', 'assignmentcode'),)


class Tmpautovouchersetting(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    partcode = models.IntegerField(db_column='PartCode')  # Field name made lowercase.
    typegroup = models.IntegerField(db_column='TypeGroup')  # Field name made lowercase.
    type = models.IntegerField(db_column='Type')  # Field name made lowercase.
    total = models.SmallIntegerField(db_column='Total', blank=True, null=True)  # Field name made lowercase.
    assistant = models.IntegerField(db_column='Assistant', blank=True, null=True)  # Field name made lowercase.
    detail = models.IntegerField(db_column='Detail', blank=True, null=True)  # Field name made lowercase.
    debit = models.CharField(db_column='Debit', max_length=500, blank=True, null=True)  # Field name made lowercase.
    credit = models.CharField(db_column='Credit', max_length=500, blank=True, null=True)  # Field name made lowercase.
    aggregate = models.IntegerField(db_column='Aggregate')  # Field name made lowercase.
    comment = models.CharField(db_column='Comment', max_length=500, blank=True, null=True)  # Field name made lowercase.
    customwhereclause = models.CharField(db_column='CustomWhereClause', max_length=2000, blank=True, null=True)  # Field name made lowercase.
    clientnumber = models.SmallIntegerField(db_column='ClientNumber')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tmpAutoVoucherSetting'


class TmpautoStaffoutputget(models.Model):
    overtime = models.DecimalField(max_digits=23, decimal_places=8, blank=True, null=True)
    holiday = models.DecimalField(db_column='Holiday', max_digits=23, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    late = models.DecimalField(max_digits=23, decimal_places=8, blank=True, null=True)
    withoutsalary = models.DecimalField(max_digits=23, decimal_places=8, blank=True, null=True)
    withsalary = models.DecimalField(max_digits=23, decimal_places=8, blank=True, null=True)
    duty = models.DecimalField(db_column='Duty', max_digits=23, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    absence = models.IntegerField(db_column='Absence', blank=True, null=True)  # Field name made lowercase.
    withoutsalarytime = models.DecimalField(db_column='WithOutSalaryTime', max_digits=23, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    withoutsalaryday = models.DecimalField(db_column='WithOutSalaryDay', max_digits=23, decimal_places=8, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tmpAuto_StaffoutPutGet'


class Tmpbooks(models.Model):
    sanadtype = models.SmallIntegerField(db_column='SanadType', blank=True, null=True)  # Field name made lowercase.
    code = models.IntegerField(blank=True, null=True)
    date = models.CharField(db_column='Date', max_length=10, blank=True, null=True)  # Field name made lowercase.
    comment = models.CharField(db_column='Comment', max_length=500, blank=True, null=True)  # Field name made lowercase.
    bed = models.DecimalField(db_column='Bed', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    bes = models.DecimalField(db_column='Bes', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    remain = models.DecimalField(db_column='Remain', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=10, blank=True, null=True)  # Field name made lowercase.
    radif = models.IntegerField(db_column='Radif', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tmpBooks'


class Tmpcheckbandreport(models.Model):
    id_check = models.CharField(db_column='ID_CHeck', max_length=50, blank=True, null=True)  # Field name made lowercase.
    date2 = models.CharField(db_column='Date2', max_length=10, blank=True, null=True)  # Field name made lowercase.
    status = models.SmallIntegerField(db_column='Status', blank=True, null=True)  # Field name made lowercase.
    perid = models.IntegerField(db_column='PerId', blank=True, null=True)  # Field name made lowercase.
    date1 = models.CharField(db_column='Date1', max_length=10, blank=True, null=True)  # Field name made lowercase.
    amount = models.DecimalField(db_column='Amount', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    comment = models.CharField(db_column='Comment', max_length=500, blank=True, null=True)  # Field name made lowercase.
    bankcode = models.IntegerField(db_column='BankCode', blank=True, null=True)  # Field name made lowercase.
    pertype = models.SmallIntegerField(db_column='PerType', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tmpCheckBandReport'


class Tmpcostlist(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    type = models.SmallIntegerField(db_column='Type')  # Field name made lowercase.
    status = models.BooleanField(db_column='Status')  # Field name made lowercase.
    typecode = models.IntegerField(db_column='TypeCode')  # Field name made lowercase.
    costlevelcode = models.IntegerField(db_column='CostLevelCode')  # Field name made lowercase.
    cost = models.DecimalField(db_column='Cost', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    default = models.BooleanField(db_column='Default', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tmpCostList'


class TmpfactFo(models.Model):
    code = models.IntegerField(db_column='Code', primary_key=True)  # Field name made lowercase. The composite primary key (Code, Com_Index) found, that is not supported. The first column is selected.
    shakhs_code = models.SmallIntegerField(db_column='Shakhs_Code', blank=True, null=True)  # Field name made lowercase.
    visitor_code = models.SmallIntegerField(blank=True, null=True)
    tavasot = models.CharField(max_length=50, blank=True, null=True)
    tarikh = models.CharField(max_length=50, blank=True, null=True)
    mablagh_factor = models.DecimalField(max_digits=23, decimal_places=9, blank=True, null=True)
    takhfif = models.DecimalField(max_digits=23, decimal_places=9, blank=True, null=True)
    ranandeh_code = models.SmallIntegerField(blank=True, null=True)
    mablagh_haml = models.DecimalField(max_digits=23, decimal_places=9, blank=True, null=True)
    sanad_code = models.IntegerField(blank=True, null=True)
    sharh = models.CharField(max_length=500, blank=True, null=True)
    sabt_hazineh = models.SmallIntegerField(db_column='Sabt_Hazineh', blank=True, null=True)  # Field name made lowercase.
    mablagh_visit = models.DecimalField(db_column='Mablagh_visit', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    status = models.SmallIntegerField(blank=True, null=True)
    sanad = models.IntegerField(blank=True, null=True)
    tarikhvosoul = models.CharField(max_length=50, blank=True, null=True)
    tasviye = models.SmallIntegerField(blank=True, null=True)
    naghdi = models.SmallIntegerField(blank=True, null=True)
    lockfact = models.SmallIntegerField(db_column='LockFact', blank=True, null=True)  # Field name made lowercase.
    com_index = models.IntegerField(db_column='Com_Index')  # Field name made lowercase.
    extname = models.CharField(db_column='extName', max_length=150, blank=True, null=True)  # Field name made lowercase.
    charge = models.DecimalField(db_column='Charge', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    tax = models.DecimalField(db_column='Tax', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    tarikhtahvil = models.CharField(db_column='TarikhTahvil', max_length=10, blank=True, null=True)  # Field name made lowercase.
    tahvil = models.BooleanField(db_column='Tahvil', blank=True, null=True)  # Field name made lowercase.
    noetasviye = models.SmallIntegerField(db_column='NoeTasviye', blank=True, null=True)  # Field name made lowercase.
    takhfif_type = models.BooleanField(db_column='Takhfif_Type', blank=True, null=True)  # Field name made lowercase.
    takhfif_percent = models.DecimalField(db_column='Takhfif_Percent', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tmpFact_Fo'
        unique_together = (('code', 'com_index'),)


class TmpfactFoDetail(models.Model):
    id = models.BigAutoField(primary_key=True)
    code = models.ForeignKey(FactFo, on_delete=models.DO_NOTHING, db_column='code')
    radif = models.SmallIntegerField()
    an_code = models.ForeignKey(Stores, on_delete=models.DO_NOTHING, db_column='an_code', blank=True, null=True)
    kala_code = models.IntegerField()
    sharh = models.CharField(max_length=500, blank=True, null=True)
    meghdar = models.DecimalField(max_digits=23, decimal_places=8, blank=True, null=True)
    naghdi = models.DecimalField(max_digits=23, decimal_places=9, blank=True, null=True)
    reval = models.IntegerField(blank=True, null=True)
    vaziyat = models.SmallIntegerField()
    status = models.SmallIntegerField()
    type = models.SmallIntegerField(db_column='Type', blank=True, null=True)  # Field name made lowercase.
    darsad_vis = models.DecimalField(max_digits=23, decimal_places=8, blank=True, null=True)
    tool = models.DecimalField(max_digits=23, decimal_places=8, blank=True, null=True)
    arz = models.DecimalField(max_digits=23, decimal_places=8, blank=True, null=True)
    tedad = models.IntegerField(blank=True, null=True)
    meghdar2 = models.DecimalField(max_digits=23, decimal_places=8, blank=True, null=True)
    ghotr = models.DecimalField(max_digits=23, decimal_places=8, blank=True, null=True)
    com_index = models.IntegerField()
    toolidcode = models.IntegerField(db_column='ToolidCode', blank=True, null=True)  # Field name made lowercase.
    userprice = models.DecimalField(db_column='UserPrice', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    chargepercent = models.DecimalField(db_column='ChargePercent', max_digits=23, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    taxpercent = models.DecimalField(db_column='TaxPercent', max_digits=23, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    takhfif = models.DecimalField(max_digits=23, decimal_places=9, blank=True, null=True)
    ordercode = models.IntegerField(db_column='OrderCode', blank=True, null=True)  # Field name made lowercase.
    takhfiftype = models.BooleanField(db_column='TakhfifType')  # Field name made lowercase.
    takhfifasexpense = models.BooleanField(db_column='TakhfifAsExpense', blank=True, null=True)  # Field name made lowercase.
    off_user = models.DecimalField(db_column='Off_User', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    off_sys = models.DecimalField(db_column='Off_Sys', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    cost_entery_type = models.BooleanField(db_column='Cost_Entery_Type', blank=True, null=True)  # Field name made lowercase.
    totalcost = models.DecimalField(db_column='TotalCost', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    currcode = models.IntegerField(db_column='CurrCode', blank=True, null=True)  # Field name made lowercase.
    currrate = models.DecimalField(db_column='CurrRate', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    barcode = models.CharField(db_column='Barcode', max_length=50, blank=True, null=True)  # Field name made lowercase.
    gifttype = models.SmallIntegerField(db_column='GiftType', blank=True, null=True)  # Field name made lowercase.
    promotioncode = models.IntegerField(db_column='PromotionCode', blank=True, null=True)  # Field name made lowercase.
    offvaluetype = models.SmallIntegerField(db_column='OffValueType', blank=True, null=True)  # Field name made lowercase.
    goldprice = models.DecimalField(db_column='GoldPrice', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    wages = models.DecimalField(db_column='Wages', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    sellerprofit = models.DecimalField(db_column='SellerProfit', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    rightofaction = models.DecimalField(db_column='RightOfAction', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    goldselltaxpercent = models.DecimalField(db_column='GoldSellTaxPercent', max_digits=23, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    currencytype = models.CharField(db_column='CurrencyType', max_length=3, blank=True, null=True)  # Field name made lowercase.
    exchangeratewithrial = models.DecimalField(db_column='ExchangeRateWithRial', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Fact_Fo_Detail'
        unique_together = (('code', 'radif'),)

class Tmpgardesh(models.Model):
    date = models.CharField(db_column='Date', max_length=10, blank=True, null=True)  # Field name made lowercase.
    type = models.SmallIntegerField(db_column='Type', blank=True, null=True)  # Field name made lowercase.
    code = models.CharField(db_column='Code', max_length=50, blank=True, null=True)  # Field name made lowercase.
    comment = models.CharField(db_column='Comment', max_length=500, blank=True, null=True)  # Field name made lowercase.
    bes = models.DecimalField(db_column='Bes', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    bed = models.DecimalField(db_column='Bed', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    bagh = models.DecimalField(db_column='Bagh', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(max_length=50, blank=True, null=True)
    radif = models.BigIntegerField(db_column='Radif', blank=True, null=True)  # Field name made lowercase.
    vouchercode = models.IntegerField(db_column='VoucherCode', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tmpGardesh'


class Tmpgardeshhesab(models.Model):
    code = models.IntegerField(blank=True, null=True)
    radif = models.IntegerField(db_column='Radif', blank=True, null=True)  # Field name made lowercase.
    bed = models.DecimalField(db_column='Bed', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    bes = models.DecimalField(db_column='Bes', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    sanadcomment = models.CharField(db_column='SanadComment', max_length=500, blank=True, null=True)  # Field name made lowercase.
    rowcomment = models.CharField(db_column='RowComment', max_length=500, blank=True, null=True)  # Field name made lowercase.
    date = models.CharField(db_column='Date', max_length=10, blank=True, null=True)  # Field name made lowercase.
    remain = models.DecimalField(db_column='Remain', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tmpGardeshHesab'


class Tmpgardeshkholaseashkhas(models.Model):
    date = models.CharField(db_column='Date', max_length=10, blank=True, null=True)  # Field name made lowercase.
    type = models.SmallIntegerField(db_column='Type', blank=True, null=True)  # Field name made lowercase.
    code = models.CharField(db_column='Code', max_length=50, blank=True, null=True)  # Field name made lowercase.
    comment = models.CharField(db_column='Comment', max_length=500, blank=True, null=True)  # Field name made lowercase.
    bes = models.DecimalField(db_column='Bes', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    bed = models.DecimalField(db_column='Bed', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    bagh = models.DecimalField(db_column='Bagh', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(max_length=50, blank=True, null=True)
    radif = models.BigIntegerField(db_column='Radif', blank=True, null=True)  # Field name made lowercase.
    vouchercode = models.IntegerField(db_column='VoucherCode', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tmpGardeshKholaseAshkhas'


class TmpgetRecieve(models.Model):
    code = models.IntegerField(db_column='Code', primary_key=True)  # Field name made lowercase. The composite primary key (Code, Type) found, that is not supported. The first column is selected.
    percode = models.IntegerField(db_column='PerCode')  # Field name made lowercase.
    amount = models.DecimalField(db_column='Amount', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    comment = models.CharField(db_column='Comment', max_length=500, blank=True, null=True)  # Field name made lowercase.
    date = models.CharField(db_column='Date', max_length=10)  # Field name made lowercase.
    status = models.SmallIntegerField(db_column='Status', blank=True, null=True)  # Field name made lowercase.
    type = models.SmallIntegerField(db_column='Type')  # Field name made lowercase.
    fish = models.CharField(db_column='Fish', max_length=50, blank=True, null=True)  # Field name made lowercase.
    op_type = models.SmallIntegerField(db_column='OP_Type')  # Field name made lowercase.
    lmod = models.DecimalField(db_column='LMod', max_digits=23, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    jam = models.DecimalField(db_column='Jam', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    takhfif = models.DecimalField(db_column='Takhfif', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    lsit = models.SmallIntegerField(blank=True, null=True)
    status_fact = models.IntegerField(db_column='Status_Fact', blank=True, null=True)  # Field name made lowercase.
    sandogh_code = models.ForeignKey(SandoghTbl, on_delete=models.DO_NOTHING, db_column='Sandogh_Code', blank=True, null=True)  # Field name made lowercase.
    tavasot = models.CharField(db_column='Tavasot', max_length=50, blank=True, null=True)  # Field name made lowercase.
    vouchercode = models.IntegerField(db_column='VoucherCode', blank=True, null=True)  # Field name made lowercase.
    owner_type = models.SmallIntegerField(db_column='Owner_Type', blank=True, null=True)  # Field name made lowercase.
    visitor_code = models.IntegerField(db_column='Visitor_Code', blank=True, null=True)  # Field name made lowercase.
    expcentercode = models.IntegerField(db_column='ExpCenterCode', blank=True, null=True)  # Field name made lowercase.
    refrenceid = models.CharField(db_column='RefrenceID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    flag = models.SmallIntegerField(blank=True, null=True)
    currcode = models.IntegerField(db_column='CurrCode', blank=True, null=True)  # Field name made lowercase.
    currrate = models.DecimalField(db_column='CurrRate', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    createdtime = models.CharField(db_column='CreatedTime', max_length=5, blank=True, null=True)  # Field name made lowercase.
    createddate = models.CharField(db_column='CreatedDate', max_length=10, blank=True, null=True)  # Field name made lowercase.
    modifiedtime = models.CharField(db_column='ModifiedTime', max_length=5, blank=True, null=True)  # Field name made lowercase.
    modifieddate = models.CharField(db_column='ModifiedDate', max_length=10, blank=True, null=True)  # Field name made lowercase.
    usercreated = models.IntegerField(db_column='UserCreated')  # Field name made lowercase.
    usermodified = models.IntegerField(db_column='UserModified', blank=True, null=True)  # Field name made lowercase.
    global_id = models.IntegerField(db_column='Global_ID')  # Field name made lowercase.
    owner = models.IntegerField(db_column='Owner')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tmpGet_Recieve'
        unique_together = (('code', 'type'),)


class Tmpmemberfamily(models.Model):
    code = models.IntegerField(db_column='Code', primary_key=True)  # Field name made lowercase.
    membercode = models.IntegerField(db_column='MemberCode')  # Field name made lowercase.
    type = models.BooleanField(db_column='Type', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=100, blank=True, null=True)  # Field name made lowercase.
    sex = models.BooleanField(db_column='Sex', blank=True, null=True)  # Field name made lowercase.
    fathername = models.CharField(db_column='FatherName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    birthdate = models.CharField(db_column='BirthDate', max_length=10, blank=True, null=True)  # Field name made lowercase.
    idnum = models.CharField(db_column='IDNum', max_length=50, blank=True, null=True)  # Field name made lowercase.
    nationalid = models.CharField(db_column='NationalID', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tmpMemberFamily'


class Tmporderdetail(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    ordercode = models.IntegerField(db_column='OrderCode')  # Field name made lowercase.
    storecode = models.SmallIntegerField(db_column='Storecode', blank=True, null=True)  # Field name made lowercase.
    goodcode = models.IntegerField(db_column='Goodcode')  # Field name made lowercase.
    comment = models.CharField(db_column='Comment', max_length=500, blank=True, null=True)  # Field name made lowercase.
    amount = models.DecimalField(db_column='Amount', max_digits=23, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    naghdi = models.DecimalField(max_digits=23, decimal_places=9, blank=True, null=True)
    tool = models.DecimalField(max_digits=23, decimal_places=8, blank=True, null=True)
    arz = models.DecimalField(max_digits=23, decimal_places=8, blank=True, null=True)
    tedad = models.IntegerField(blank=True, null=True)
    amount2 = models.DecimalField(db_column='Amount2', max_digits=23, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    ghotr = models.DecimalField(max_digits=23, decimal_places=8, blank=True, null=True)
    reval = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tmpOrderDetail'


class TmppishforooshDetail(models.Model):
    code = models.IntegerField(primary_key=True)  # The composite primary key (code, radif) found, that is not supported. The first column is selected.
    radif = models.SmallIntegerField()
    an_code = models.SmallIntegerField(blank=True, null=True)
    kala_code = models.IntegerField(blank=True, null=True)
    sharh = models.CharField(max_length=500, blank=True, null=True)
    meghdar = models.DecimalField(max_digits=23, decimal_places=8, blank=True, null=True)
    naghdi = models.DecimalField(max_digits=23, decimal_places=9, blank=True, null=True)
    reval = models.IntegerField(blank=True, null=True)
    vaziyat = models.SmallIntegerField(blank=True, null=True)
    status = models.SmallIntegerField(blank=True, null=True)
    tool = models.DecimalField(max_digits=23, decimal_places=8, blank=True, null=True)
    arz = models.DecimalField(max_digits=23, decimal_places=8, blank=True, null=True)
    tedad = models.IntegerField(blank=True, null=True)
    meghdar2 = models.DecimalField(max_digits=23, decimal_places=8, blank=True, null=True)
    ghotr = models.DecimalField(max_digits=23, decimal_places=8, blank=True, null=True)
    com_index = models.IntegerField()
    userprice = models.DecimalField(db_column='UserPrice', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    chargepercent = models.DecimalField(db_column='ChargePercent', max_digits=23, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    taxpercent = models.DecimalField(db_column='TaxPercent', max_digits=23, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    takhfif = models.DecimalField(db_column='Takhfif', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tmpPishForoosh_Detail'
        unique_together = (('code', 'radif'),)


class Tmpprintssettings(models.Model):
    partname = models.CharField(db_column='PartName', primary_key=True, max_length=20)  # Field name made lowercase. The composite primary key (PartName, TypeName, ManageType, UserCode) found, that is not supported. The first column is selected.
    typename = models.CharField(db_column='TypeName', max_length=300)  # Field name made lowercase.
    comment = models.CharField(db_column='Comment', max_length=500, blank=True, null=True)  # Field name made lowercase.
    meghdar = models.DecimalField(db_column='Meghdar', max_digits=23, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    managetype = models.SmallIntegerField(db_column='ManageType')  # Field name made lowercase.
    usercode = models.IntegerField(db_column='UserCode')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tmpPrintsSettings'
        unique_together = (('partname', 'typename', 'managetype', 'usercode'),)


class Tmprecdeduction(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    recruitmentcode = models.IntegerField(db_column='RecruitmentCode')  # Field name made lowercase.
    itemcode = models.IntegerField(db_column='ItemCode')  # Field name made lowercase.
    cost = models.DecimalField(db_column='Cost', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tmpRecDeduction'


class Tmprecfiscal(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    recruitmentcode = models.IntegerField(db_column='RecruitmentCode')  # Field name made lowercase.
    itemcode = models.IntegerField(db_column='ItemCode')  # Field name made lowercase.
    cost = models.DecimalField(db_column='Cost', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tmpRecFiscal'


class Tmpreceiptdetail(models.Model):
    code = models.IntegerField(db_column='Code', primary_key=True)  # Field name made lowercase. The composite primary key (Code, ReceiptCode) found, that is not supported. The first column is selected.
    receiptcode = models.IntegerField(db_column='ReceiptCode')  # Field name made lowercase.
    goodcode = models.IntegerField(db_column='GoodCode', blank=True, null=True)  # Field name made lowercase.
    amount = models.DecimalField(db_column='Amount', max_digits=23, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    amount2 = models.DecimalField(db_column='Amount2', max_digits=23, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    cost = models.DecimalField(db_column='Cost', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    storecode = models.IntegerField(db_column='StoreCode', blank=True, null=True)  # Field name made lowercase.
    comment = models.CharField(db_column='Comment', max_length=500, blank=True, null=True)  # Field name made lowercase.
    width = models.DecimalField(db_column='Width', max_digits=23, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    height = models.DecimalField(db_column='Height', max_digits=23, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    num = models.DecimalField(db_column='Num', max_digits=23, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    global_id = models.IntegerField(db_column='Global_ID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tmpReceiptDetail'
        unique_together = (('code', 'receiptcode'),)


class Tmprefreshautovouchers(models.Model):
    parttitle = models.CharField(db_column='PartTitle', max_length=100, blank=True, null=True)  # Field name made lowercase.
    partcode = models.IntegerField(db_column='PartCode', blank=True, null=True)  # Field name made lowercase.
    status = models.IntegerField(db_column='Status', blank=True, null=True)  # Field name made lowercase.
    voucherdate = models.CharField(db_column='VoucherDate', max_length=10, blank=True, null=True)  # Field name made lowercase.
    operationcode = models.CharField(db_column='OperationCode', max_length=50, blank=True, null=True)  # Field name made lowercase.
    date = models.CharField(max_length=10, blank=True, null=True)
    vouchercode = models.IntegerField(db_column='VoucherCode', blank=True, null=True)  # Field name made lowercase.
    lastprintdate = models.CharField(db_column='LastPrintDate', max_length=20, blank=True, null=True)  # Field name made lowercase.
    checked = models.SmallIntegerField(db_column='Checked', blank=True, null=True)  # Field name made lowercase.
    global_id = models.IntegerField(db_column='Global_ID', blank=True, null=True)  # Field name made lowercase.
    prioritytype = models.IntegerField(db_column='PriorityType', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tmpRefreshAutoVouchers'


class TmprefreshautovouchersList(models.Model):
    goodcodes = models.CharField(db_column='GoodCodes', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    date = models.CharField(db_column='Date', max_length=10, blank=True, null=True)  # Field name made lowercase.
    global_id = models.IntegerField(db_column='Global_ID', blank=True, null=True)  # Field name made lowercase.
    vouchercode = models.IntegerField(db_column='VoucherCode', blank=True, null=True)  # Field name made lowercase.
    rowchecked = models.SmallIntegerField(db_column='RowChecked', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tmpRefreshAutoVouchers_List'


class Tmprepositorydetail(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    repositorycode = models.IntegerField(db_column='RepositoryCode')  # Field name made lowercase.
    file = models.BinaryField(db_column='File')  # Field name made lowercase.
    fileaddr = models.CharField(db_column='FileAddr', max_length=200)  # Field name made lowercase.
    fileextention = models.CharField(db_column='FileExtention', max_length=5)  # Field name made lowercase.
    comment = models.CharField(db_column='Comment', max_length=500, blank=True, null=True)  # Field name made lowercase.
    holdplace = models.CharField(db_column='HoldPlace', max_length=100, blank=True, null=True)  # Field name made lowercase.
    computername = models.CharField(db_column='ComputerName', max_length=50)  # Field name made lowercase.
    modifieddate = models.CharField(db_column='ModifiedDate', max_length=10)  # Field name made lowercase.
    modifiedtime = models.CharField(db_column='ModifiedTime', max_length=5)  # Field name made lowercase.
    usermodified = models.IntegerField(db_column='UserModified')  # Field name made lowercase.
    type = models.SmallIntegerField(db_column='Type', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tmpRepositoryDetail'


class Tmpsalarybilldetail(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    salarybillcode = models.IntegerField(db_column='SalaryBillCode')  # Field name made lowercase.
    itemcode = models.IntegerField(db_column='ItemCode')  # Field name made lowercase.
    amount = models.DecimalField(db_column='Amount', max_digits=23, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    cost = models.DecimalField(db_column='Cost', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    comment = models.CharField(db_column='Comment', max_length=500, blank=True, null=True)  # Field name made lowercase.
    auto = models.BooleanField(db_column='Auto')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tmpSalaryBillDetail'


class Tmpsecondaryaccount(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    shareholdercode = models.IntegerField(db_column='ShareHolderCode')  # Field name made lowercase.
    percode = models.IntegerField(db_column='PerCode')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tmpSecondaryAccount'


class Tmpstaffoutputdetail(models.Model):
    outputcode = models.IntegerField(db_column='OutPutCode')  # Field name made lowercase.
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    amount = models.DecimalField(db_column='Amount', max_digits=23, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    type = models.BooleanField(db_column='Type')  # Field name made lowercase.
    itemcode = models.IntegerField(db_column='ItemCode')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tmpStaffOutPutDetail'


class Tmptcheckamani(models.Model):
    id_check = models.CharField(db_column='ID_Check', primary_key=True, max_length=50)  # Field name made lowercase. The composite primary key (ID_Check, Type) found, that is not supported. The first column is selected.
    percode = models.IntegerField(db_column='PerCode', blank=True, null=True)  # Field name made lowercase.
    bankname = models.CharField(db_column='BankName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    bankshobe = models.CharField(db_column='BankShobe', max_length=50, blank=True, null=True)  # Field name made lowercase.
    bankid_h = models.CharField(db_column='BankID_H', max_length=50, blank=True, null=True)  # Field name made lowercase.
    amount = models.DecimalField(db_column='Amount', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    status = models.SmallIntegerField(db_column='Status', blank=True, null=True)  # Field name made lowercase.
    type = models.SmallIntegerField(db_column='Type')  # Field name made lowercase.
    bankcode = models.IntegerField(db_column='BankCode', blank=True, null=True)  # Field name made lowercase.
    operationdate = models.CharField(db_column='OperationDate', max_length=10, blank=True, null=True)  # Field name made lowercase.
    date = models.CharField(db_column='Date', max_length=10, blank=True, null=True)  # Field name made lowercase.
    radif = models.IntegerField(db_column='Radif', blank=True, null=True)  # Field name made lowercase.
    comments = models.CharField(db_column='Comments', max_length=500, blank=True, null=True)  # Field name made lowercase.
    vouchercode = models.IntegerField(db_column='VoucherCode', blank=True, null=True)  # Field name made lowercase.
    loancode = models.IntegerField(db_column='LoanCode', blank=True, null=True)  # Field name made lowercase.
    vouchercode_back = models.IntegerField(db_column='VoucherCode_Back', blank=True, null=True)  # Field name made lowercase.
    id = models.IntegerField(db_column='ID', blank=True, null=True)  # Field name made lowercase.
    createdtime = models.CharField(db_column='CreatedTime', max_length=5)  # Field name made lowercase.
    createddate = models.CharField(db_column='CreatedDate', max_length=10)  # Field name made lowercase.
    usercreated = models.IntegerField(db_column='UserCreated')  # Field name made lowercase.
    modifiedtime = models.CharField(db_column='ModifiedTime', max_length=5, blank=True, null=True)  # Field name made lowercase.
    modifieddate = models.CharField(db_column='ModifiedDate', max_length=10, blank=True, null=True)  # Field name made lowercase.
    usermodified = models.IntegerField(db_column='UserModified', blank=True, null=True)  # Field name made lowercase.
    owner = models.IntegerField(db_column='Owner')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tmpTCheckAmani'
        unique_together = (('id_check', 'type'),)


class Tmpuserpermission(models.Model):
    userid = models.ForeignKey(Users, on_delete=models.DO_NOTHING, db_column='UserID')  # Field name made lowercase.
    partpermissionid = models.ForeignKey(Partpermission, on_delete=models.DO_NOTHING, db_column='PartPermissionID')  # Field name made lowercase.
    permission = models.BooleanField(db_column='Permission', blank=True, null=True)  # Field name made lowercase.
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tmpUserPermission'
        unique_together = (('userid', 'partpermissionid'),)


class TmpwarehousehandlingDetail(models.Model):
    whhcode = models.IntegerField(db_column='WHHCode', blank=True, null=True)  # Field name made lowercase.
    rowno = models.IntegerField(db_column='RowNo', blank=True, null=True)  # Field name made lowercase.
    goodcode = models.IntegerField(db_column='GoodCode', blank=True, null=True)  # Field name made lowercase.
    storecode = models.IntegerField(db_column='StoreCode', blank=True, null=True)  # Field name made lowercase.
    grpcode = models.IntegerField(db_column='GrpCode', blank=True, null=True)  # Field name made lowercase.
    goodname = models.CharField(db_column='GoodName', max_length=500, blank=True, null=True)  # Field name made lowercase.
    storename = models.CharField(db_column='StoreName', max_length=500, blank=True, null=True)  # Field name made lowercase.
    goodunit = models.CharField(db_column='GoodUnit', max_length=50, blank=True, null=True)  # Field name made lowercase.
    realcount = models.DecimalField(db_column='RealCount', max_digits=23, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    firstcount = models.DecimalField(db_column='FirstCount', max_digits=23, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    secondcount = models.DecimalField(db_column='SecondCount', max_digits=23, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    thirdcount = models.DecimalField(db_column='ThirdCount', max_digits=23, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    checkamount = models.SmallIntegerField(db_column='CheckAmount', blank=True, null=True)  # Field name made lowercase.
    abbname = models.CharField(db_column='AbbName', max_length=300, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tmpWareHouseHandling_Detail'


class Tmpkharid(models.Model):
    code = models.IntegerField(primary_key=True)  # The composite primary key (code, com_index) found, that is not supported. The first column is selected.
    shakhs_code = models.SmallIntegerField(blank=True, null=True)
    tarikh = models.CharField(max_length=50, blank=True, null=True)
    mablagh_factor = models.DecimalField(max_digits=23, decimal_places=9, blank=True, null=True)
    takhfif = models.DecimalField(max_digits=23, decimal_places=9, blank=True, null=True)
    sanad_code = models.IntegerField(blank=True, null=True)
    sharh = models.CharField(max_length=500, blank=True, null=True)
    status = models.SmallIntegerField(db_column='Status', blank=True, null=True)  # Field name made lowercase.
    sanad = models.IntegerField(db_column='Sanad', blank=True, null=True)  # Field name made lowercase.
    tarikhvosoul = models.CharField(max_length=50, blank=True, null=True)
    tasviye = models.SmallIntegerField(blank=True, null=True)
    com_index = models.IntegerField()
    charge = models.DecimalField(db_column='Charge', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    tax = models.DecimalField(db_column='Tax', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tmpkharid'
        unique_together = (('code', 'com_index'),)


class Tmpsanad(models.Model):
    code = models.IntegerField(primary_key=True)  # The composite primary key (code, status) found, that is not supported. The first column is selected.
    tarikh = models.CharField(max_length=10, blank=True, null=True)
    zamaem = models.SmallIntegerField(blank=True, null=True)
    sharh = models.CharField(max_length=500, blank=True, null=True)
    status = models.SmallIntegerField()
    com_index = models.IntegerField(db_column='Com_Index')  # Field name made lowercase.
    lastprintdate = models.CharField(db_column='LastPrintDate', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tmpsanad'
        unique_together = (('code', 'status'),)


class TmpsanadDetail(models.Model):
    code = models.IntegerField(primary_key=True)  # The composite primary key (code, radif) found, that is not supported. The first column is selected.
    radif = models.SmallIntegerField()
    kol = models.SmallIntegerField(blank=True, null=True)
    moin = models.SmallIntegerField(blank=True, null=True)
    tafzili = models.IntegerField(blank=True, null=True)
    sharh = models.CharField(max_length=500, blank=True, null=True)
    status = models.SmallIntegerField(blank=True, null=True)
    bed = models.DecimalField(max_digits=23, decimal_places=9, blank=True, null=True)
    bes = models.DecimalField(max_digits=23, decimal_places=9, blank=True, null=True)
    sanad_code = models.CharField(db_column='Sanad_Code', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sanad_type = models.IntegerField(db_column='Sanad_Type', blank=True, null=True)  # Field name made lowercase.
    meghdar = models.DecimalField(db_column='Meghdar', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    com_index = models.IntegerField(db_column='Com_Index')  # Field name made lowercase.
    zamaem = models.IntegerField(db_column='Zamaem', blank=True, null=True)  # Field name made lowercase.
    store = models.SmallIntegerField(db_column='Store', blank=True, null=True)  # Field name made lowercase.
    tafsili2 = models.IntegerField(db_column='Tafsili2', blank=True, null=True)  # Field name made lowercase.
    voucherdate = models.CharField(db_column='VoucherDate', max_length=10, blank=True, null=True)  # Field name made lowercase.
    operationdate = models.CharField(db_column='OperationDate', max_length=10, blank=True, null=True)  # Field name made lowercase.
    syscomment = models.CharField(db_column='SysComment', max_length=1100, blank=True, null=True)  # Field name made lowercase.
    currcode = models.IntegerField(db_column='CurrCode', blank=True, null=True)  # Field name made lowercase.
    curramount = models.DecimalField(db_column='CurrAmount', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    currrate = models.DecimalField(db_column='CurrRate', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    usercode = models.IntegerField(db_column='UserCode', blank=True, null=True)  # Field name made lowercase.
    global_id = models.IntegerField(db_column='Global_ID', blank=True, null=True)  # Field name made lowercase.
    createdtime = models.CharField(db_column='CreatedTime', max_length=5, blank=True, null=True)  # Field name made lowercase.
    createddate = models.CharField(db_column='CreatedDate', max_length=10, blank=True, null=True)  # Field name made lowercase.
    modifiedtime = models.CharField(db_column='ModifiedTime', max_length=5, blank=True, null=True)  # Field name made lowercase.
    modifieddate = models.CharField(db_column='ModifiedDate', max_length=10, blank=True, null=True)  # Field name made lowercase.
    usercreated = models.CharField(db_column='UserCreated', max_length=50, blank=True, null=True)  # Field name made lowercase.
    usermodified = models.CharField(db_column='UserModified', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tmpsanad_detail'
        unique_together = (('code', 'radif'),)


class Tmpserials(models.Model):
    date = models.CharField(max_length=50, blank=True, null=True)
    kalaname = models.CharField(max_length=153, blank=True, null=True)
    sharh = models.CharField(max_length=500, blank=True, null=True)
    meghdar = models.DecimalField(max_digits=23, decimal_places=8, blank=True, null=True)
    meghdar2 = models.DecimalField(max_digits=23, decimal_places=8, blank=True, null=True)
    percode = models.IntegerField()
    code = models.IntegerField()
    radif = models.SmallIntegerField()
    type = models.SmallIntegerField()
    kala = models.IntegerField()
    gheymat = models.DecimalField(max_digits=38, decimal_places=7, blank=True, null=True)
    pername = models.CharField(max_length=171, blank=True, null=True)
    sanadsharh = models.CharField(max_length=553, blank=True, null=True)
    varede = models.IntegerField(blank=True, null=True)
    sadere = models.IntegerField(blank=True, null=True)
    anbar = models.SmallIntegerField(db_column='Anbar')  # Field name made lowercase.
    anbar_name = models.CharField(db_column='Anbar_Name', max_length=50, blank=True, null=True)  # Field name made lowercase.
    mojod = models.IntegerField(db_column='Mojod')  # Field name made lowercase.
    expiredate_sr = models.CharField(db_column='expiredate_SR', max_length=10, blank=True, null=True)  # Field name made lowercase.
    color_sr = models.CharField(db_column='Color_SR', max_length=50, blank=True, null=True)  # Field name made lowercase.
    size_sr = models.CharField(db_column='Size_SR', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tmpserials'


class TmptmpsanadDetail1(models.Model):
    code = models.IntegerField(db_column='Code', blank=True, null=True)  # Field name made lowercase.
    kol = models.IntegerField(db_column='Kol', blank=True, null=True)  # Field name made lowercase.
    moin = models.IntegerField(db_column='Moin', blank=True, null=True)  # Field name made lowercase.
    tafzili = models.IntegerField(db_column='Tafzili', blank=True, null=True)  # Field name made lowercase.
    tafsili2 = models.IntegerField(db_column='Tafsili2', blank=True, null=True)  # Field name made lowercase.
    sharh = models.CharField(db_column='Sharh', max_length=500)  # Field name made lowercase.
    status = models.SmallIntegerField(db_column='Status', blank=True, null=True)  # Field name made lowercase.
    bed = models.DecimalField(db_column='Bed', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    bes = models.DecimalField(db_column='Bes', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    sanad_code = models.IntegerField(db_column='Sanad_Code')  # Field name made lowercase.
    sanad_type = models.IntegerField(db_column='Sanad_Type')  # Field name made lowercase.
    meghdar = models.IntegerField(db_column='Meghdar')  # Field name made lowercase.
    com_index = models.IntegerField(db_column='Com_Index')  # Field name made lowercase.
    zamaem = models.IntegerField(db_column='Zamaem')  # Field name made lowercase.
    store = models.IntegerField(db_column='Store')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tmptmpsanad_detail1'


class TmptmpsanadDetail2(models.Model):
    code = models.IntegerField(db_column='Code', blank=True, null=True)  # Field name made lowercase.
    kol = models.SmallIntegerField(db_column='Kol', blank=True, null=True)  # Field name made lowercase.
    moin = models.SmallIntegerField(db_column='Moin', blank=True, null=True)  # Field name made lowercase.
    tafzili = models.SmallIntegerField(db_column='Tafzili', blank=True, null=True)  # Field name made lowercase.
    tafsili2 = models.IntegerField(db_column='Tafsili2', blank=True, null=True)  # Field name made lowercase.
    sharh = models.CharField(db_column='Sharh', max_length=500)  # Field name made lowercase.
    status = models.SmallIntegerField(db_column='Status', blank=True, null=True)  # Field name made lowercase.
    bed = models.DecimalField(db_column='Bed', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    bes = models.DecimalField(db_column='Bes', max_digits=23, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    sanad_code = models.IntegerField(db_column='Sanad_Code')  # Field name made lowercase.
    sanad_type = models.IntegerField(db_column='Sanad_Type')  # Field name made lowercase.
    meghdar = models.IntegerField(db_column='Meghdar')  # Field name made lowercase.
    com_index = models.IntegerField(db_column='Com_Index')  # Field name made lowercase.
    zamaem = models.IntegerField(db_column='Zamaem')  # Field name made lowercase.
    store = models.IntegerField(db_column='Store')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tmptmpsanad_detail2'


class VisitorType(models.Model):
    code = models.IntegerField()
    name = models.CharField(db_column='Name', max_length=50, blank=True, null=True)  # Field name made lowercase.
    percent = models.DecimalField(max_digits=23, decimal_places=8, blank=True, null=True)
    price = models.DecimalField(max_digits=23, decimal_places=9, blank=True, null=True)
    type = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'visitor_type'


class VoiceSendMessages(models.Model):
    idmessage = models.BigIntegerField(primary_key=True)
    title = models.CharField(max_length=50, blank=True, null=True)
    idvoice = models.BigIntegerField(blank=True, null=True)
    datesend = models.CharField(max_length=10, blank=True, null=True)
    timesend = models.CharField(max_length=7, blank=True, null=True)
    date = models.CharField(max_length=10, blank=True, null=True)
    time = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'voice_send_messages'


# Import the custom user model to make it available to Django
from .custom_user import LegacyUser



