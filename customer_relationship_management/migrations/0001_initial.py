# Generated by Django 4.2.4 on 2023-12-30 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='accInsert',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('accountowner', models.CharField(max_length=100)),
                ('rating', models.CharField(max_length=100)),
                ('accountname', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('accountsite', models.CharField(max_length=100)),
                ('fax', models.CharField(max_length=100)),
                ('parentaccount', models.CharField(max_length=100)),
                ('website', models.CharField(max_length=100)),
                ('accountnumber', models.CharField(max_length=100)),
                ('tickersymbol', models.CharField(max_length=100)),
                ('accounttype', models.CharField(max_length=100)),
                ('ownership', models.CharField(max_length=100)),
                ('industry', models.CharField(max_length=100)),
                ('employees', models.CharField(max_length=100)),
                ('annualrevenue', models.CharField(max_length=100)),
                ('siccode', models.CharField(max_length=100)),
                ('exchangerate', models.CharField(max_length=100)),
                ('currency', models.CharField(max_length=100)),
                ('billingstreet', models.CharField(max_length=100)),
                ('shippingstreet', models.CharField(max_length=100)),
                ('billingcity', models.CharField(max_length=100)),
                ('shippingcity', models.CharField(max_length=100)),
                ('billingstate', models.CharField(max_length=100)),
                ('shippingstate', models.CharField(max_length=100)),
                ('billingcode', models.CharField(max_length=100)),
                ('shippingcode', models.CharField(max_length=100)),
                ('billingcountry', models.CharField(max_length=100)),
                ('shippingcountry', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'account',
            },
        ),
        migrations.CreateModel(
            name='billInsert',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invoiceowner', models.CharField(max_length=100)),
                ('subject', models.CharField(max_length=100)),
                ('invoicedate', models.CharField(max_length=100)),
                ('duedate', models.CharField(max_length=100)),
                ('salescommision', models.CharField(max_length=100)),
                ('accountname', models.CharField(max_length=100)),
                ('contactname', models.CharField(max_length=100)),
                ('dealname', models.CharField(max_length=100)),
                ('salesorder', models.CharField(max_length=100)),
                ('purchaseorder', models.CharField(max_length=100)),
                ('exciseduty', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=100)),
                ('currency', models.CharField(max_length=100)),
                ('productname', models.CharField(max_length=100)),
                ('quantity', models.CharField(max_length=100)),
                ('listprice', models.CharField(max_length=100)),
                ('amount', models.CharField(max_length=100)),
                ('discount', models.CharField(max_length=100)),
                ('tax', models.CharField(max_length=100)),
                ('total', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'bill',
            },
        ),
        migrations.CreateModel(
            name='conInsert',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contactowner', models.CharField(max_length=100)),
                ('leadsource', models.CharField(max_length=100)),
                ('firstname', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('accountname', models.CharField(max_length=100)),
                ('vendorname', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('department', models.CharField(max_length=100)),
                ('otherphone', models.CharField(max_length=100)),
                ('homephone', models.CharField(max_length=100)),
                ('mobile', models.CharField(max_length=100)),
                ('fax', models.CharField(max_length=100)),
                ('assitant', models.CharField(max_length=100)),
                ('dateofbirth', models.CharField(max_length=100)),
                ('asstphone', models.CharField(max_length=100)),
                ('emailoptout', models.CharField(max_length=100)),
                ('skypeid', models.CharField(max_length=100)),
                ('secondaryemail', models.CharField(max_length=100)),
                ('twitter', models.CharField(max_length=100)),
                ('reportingto', models.CharField(max_length=100)),
                ('mailingstreet', models.CharField(max_length=100)),
                ('mailingcity', models.CharField(max_length=100)),
                ('mailingstate', models.CharField(max_length=100)),
                ('mailingzip', models.CharField(max_length=100)),
                ('mailingcountry', models.CharField(max_length=100)),
                ('otherstreet', models.CharField(max_length=100)),
                ('othercity', models.CharField(max_length=100)),
                ('otherstate', models.CharField(max_length=100)),
                ('otherzip', models.CharField(max_length=100)),
                ('othercountry', models.CharField(max_length=100)),
                ('descriptioninformation', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'contact',
            },
        ),
        migrations.CreateModel(
            name='dealInsert',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dealowner', models.CharField(max_length=50)),
                ('amount', models.CharField(max_length=45)),
                ('dealname', models.CharField(max_length=45)),
                ('closingdate', models.CharField(max_length=45)),
                ('accountname', models.CharField(max_length=45)),
                ('pipeline', models.CharField(max_length=45)),
                ('type', models.CharField(max_length=45)),
                ('stage', models.CharField(max_length=45)),
                ('nextstep', models.CharField(max_length=45)),
                ('probability', models.CharField(max_length=45)),
                ('leadsource', models.CharField(max_length=45)),
                ('expectedrevenue', models.CharField(max_length=45)),
                ('contactname', models.CharField(max_length=45)),
                ('campaignsource', models.CharField(max_length=45)),
                ('projectdelivered', models.CharField(max_length=45)),
                ('proposalconfirmed', models.CharField(max_length=45)),
                ('closelostdate', models.CharField(max_length=45)),
                ('exchangerate', models.CharField(max_length=45)),
                ('currency', models.CharField(max_length=45)),
                ('enquirydate', models.CharField(max_length=45)),
                ('geographyofoperations', models.CharField(max_length=45)),
                ('businessactivity', models.CharField(max_length=45)),
                ('numberofoffices', models.CharField(max_length=45)),
                ('turnover', models.CharField(max_length=45)),
                ('numberofemployees', models.CharField(max_length=45)),
                ('numberofcustomers', models.CharField(max_length=45)),
                ('meetingdate', models.CharField(max_length=45)),
                ('serviceslookingfor', models.CharField(max_length=45)),
                ('meetingstatus', models.CharField(max_length=45)),
                ('reasonfordelayed', models.CharField(max_length=45)),
                ('proposalsentdate', models.CharField(max_length=45)),
                ('firstfollowupdate', models.CharField(max_length=45)),
                ('secondfollowupdate', models.CharField(max_length=45)),
                ('description', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'deal',
            },
        ),
        migrations.CreateModel(
            name='Lead',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('leadowner', models.CharField(max_length=100)),
                ('leadsource', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=100)),
                ('emailoptout', models.CharField(max_length=100)),
                ('firstname', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('company', models.CharField(max_length=100)),
                ('mobile', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('website', models.CharField(max_length=100)),
                ('industry', models.CharField(max_length=100)),
                ('noofemp', models.CharField(max_length=100)),
                ('annualrevenue', models.CharField(max_length=100)),
                ('currency', models.CharField(max_length=100)),
                ('exchangerate', models.CharField(max_length=100)),
                ('leadstatus', models.CharField(max_length=100)),
                ('rating', models.CharField(max_length=100)),
                ('street', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('zipcode', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('businesscategory', models.CharField(max_length=100)),
                ('descriptionofbusinessactivity', models.TextField(blank=True, null=True)),
                ('typeofcompany', models.CharField(max_length=100)),
                ('noofvisarequired', models.CharField(max_length=100)),
                ('typeofshareholder', models.CharField(max_length=100)),
                ('preferredjurisdiction', models.CharField(max_length=100)),
                ('officespacerequired', models.CharField(max_length=100)),
                ('remarks', models.CharField(max_length=100)),
                ('preferredfreezone', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='saleInsert',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('salesowner', models.CharField(max_length=100)),
                ('dealname', models.CharField(max_length=100)),
                ('subject', models.CharField(max_length=100)),
                ('purchaseorder', models.CharField(max_length=100)),
                ('customernumber', models.CharField(max_length=100)),
                ('duedate', models.CharField(max_length=100)),
                ('quotename', models.CharField(max_length=100)),
                ('contactname', models.CharField(max_length=100)),
                ('pending', models.CharField(max_length=100)),
                ('exciseduty', models.CharField(max_length=100)),
                ('carrier', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=100)),
                ('salescommision', models.CharField(max_length=100)),
                ('exchangerate', models.CharField(max_length=100)),
                ('accountname', models.CharField(max_length=100)),
                ('currency', models.CharField(max_length=100)),
                ('billingstreet', models.CharField(max_length=100)),
                ('shippingstreet', models.CharField(max_length=100)),
                ('billingcity', models.CharField(max_length=100)),
                ('shippingcity', models.CharField(max_length=100)),
                ('billingstate', models.CharField(max_length=100)),
                ('shippingstate', models.CharField(max_length=100)),
                ('billingcode', models.CharField(max_length=100)),
                ('shippingcode', models.CharField(max_length=100)),
                ('billingcountry', models.CharField(max_length=100)),
                ('shippingcountry', models.CharField(max_length=100)),
                ('sno', models.CharField(max_length=100)),
                ('productname', models.CharField(max_length=100)),
                ('quantity', models.CharField(max_length=100)),
                ('listedprice', models.CharField(max_length=100)),
                ('amount', models.CharField(max_length=100)),
                ('discount', models.CharField(max_length=100)),
                ('tax', models.CharField(max_length=100)),
                ('total', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
                ('termsandconditions', models.CharField(max_length=100)),
                ('salesorderdescription', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'sales',
            },
        ),
        migrations.CreateModel(
            name='stdInsert',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('leadowner', models.CharField(max_length=100)),
                ('leadsource', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=100)),
                ('emailoptout', models.CharField(max_length=100)),
                ('firstname', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('company', models.CharField(max_length=100)),
                ('mobile', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('website', models.CharField(max_length=100)),
                ('industry', models.CharField(max_length=100)),
                ('noofemp', models.CharField(max_length=100)),
                ('annualrevenue', models.CharField(max_length=100)),
                ('currency', models.CharField(max_length=100)),
                ('exchangerate', models.CharField(max_length=100)),
                ('leadstatus', models.CharField(max_length=100)),
                ('rating', models.CharField(max_length=100)),
                ('street', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('zipcode', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('businesscategory', models.CharField(max_length=100)),
                ('descriptionofbusinessactivity', models.CharField(max_length=100)),
                ('typeofcompany', models.CharField(max_length=100)),
                ('noofvisarequired', models.CharField(max_length=100)),
                ('typeofshareholder', models.CharField(max_length=100)),
                ('preferredjurisdiction', models.CharField(max_length=100)),
                ('officespacerequired', models.CharField(max_length=100)),
                ('remarks', models.CharField(max_length=100)),
                ('preferredfreezone', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'admission',
            },
        ),
        migrations.CreateModel(
            name='taskInsert',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('taskowner', models.CharField(max_length=100)),
                ('subject', models.CharField(max_length=100)),
                ('duedate', models.CharField(max_length=100)),
                ('choose', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=100)),
                ('priority', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'task',
            },
        ),
    ]
