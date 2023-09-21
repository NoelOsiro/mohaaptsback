from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token
from rest_framework import status
from properties.models import Property
from tenants.models import ServiceRequest, Tenant
from transactions.models import Transaction

class YourViewTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.token = Token.objects.create(user=self.user)

        # Create sample data for testing (adjust fields as needed)
        self.tenant = Tenant.objects.create(full_name='Tenant Name', email='tenant@example.com', phone_number='1234567890')
        self.service_request = ServiceRequest.objects.create(tenant=self.tenant, description='Test request', request_date='2023-09-19')
        self.property = Property.objects.create(name='Property Name', property_type='Residential', price=1000, square_feet=1500, no_bedrooms=3)
        self.transaction = Transaction.objects.create(description='Test transaction', amount=500, transaction_type='Income', property=self.property, tenant=self.tenant, date='2023-09-19')

    def test_login_view(self):
        # Test user login
        response = self.client.post('/login/', {'username': 'testuser', 'password': 'testpassword'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('token', response.data)

    def test_logout_view(self):
        # Test user logout
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        response = self.client.post('/logout/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('message', response.data)
    
    def test_tenant_viewset(self):
        # Test TenantViewSet
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        
        # Create a new tenant
        response = self.client.post('/tenants/', {'full_name': 'New Tenant', 'email': 'newtenant@example.com', 'phone_number': '9876543210'})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        tenant_id = response.data['id']

        # Retrieve the created tenant
        response = self.client.get(f'/tenants/{tenant_id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['full_name'], 'New Tenant')

        # Update the tenant
        response = self.client.put(f'/tenants/{tenant_id}/', {'full_name': 'Updated Tenant', 'email': 'newtenant@example.com', 'phone_number': '9876543210'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['full_name'], 'Updated Tenant')

        # Delete the tenant
        response = self.client.delete(f'/tenants/{tenant_id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_service_request_viewset(self):
        # Test ServiceRequestViewSet
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        
        # Create a new service request
        response = self.client.post('/service-requests/', {'tenant': self.tenant.id, 'description': 'New request', 'request_date':'2023-09-19'})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        request_id = response.data['id']

        # Retrieve the created service request
        response = self.client.get(f'/service-requests/{request_id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['description'], 'New request')

        # Update the service request
        response = self.client.put(f'/service-requests/{request_id}/', {'description': 'Updated request','tenant': self.tenant.id,'request_date':'2023-09-19'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['description'], 'Updated request')

        # Delete the service request
        response = self.client.delete(f'/service-requests/{request_id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_property_viewset(self):
        # Test PropertyViewSet
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        
        # Create a new property
        response = self.client.post('/properties/', {'name': 'New Property', 'property_type': 'commercial', 'price': 1500, 'square_feet': 2000, 'address': '123 Main street', 'description': '2 bedroom bungalow'})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        property_id = response.data['id']

        # Retrieve the created property
        response = self.client.get(f'/properties/{property_id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'New Property')

        # Update the property
        response = self.client.put(f'/properties/{property_id}/', {'name': 'Updated Property', 'property_type': 'commercial', 'price': 1500, 'square_feet': 2000, 'address': '123 Main street', 'description': '2 bedroom bungalow'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Updated Property')

        # Delete the property
        response = self.client.delete(f'/properties/{property_id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_transaction_viewset(self):
        # Test TransactionViewSet
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        
        # Create a new transaction
        response = self.client.post('/transactions/', {'description': 'New transaction', 'amount': 800,'date':'2023-09-19', 'transaction_type': 'expense', 'property': self.property.id, 'tenant': self.tenant.id})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        transaction_id = response.data['id']

        # Retrieve the created transaction
        response = self.client.get(f'/transactions/{transaction_id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['description'], 'New transaction')

        # Update the transaction
        response = self.client.put(f'/transactions/{transaction_id}/', {'description': 'Updated transaction', 'amount': 800,'date':'2023-09-19', 'transaction_type': 'expense', 'property': self.property.id, 'tenant': self.tenant.id})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['description'], 'Updated transaction')

        # Delete the transaction
        response = self.client.delete(f'/transactions/{transaction_id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
