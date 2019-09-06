class UserProfile:

    types = {
        'login': str,
        'email': str,
        'employeeNumber': str,
        'secondEmail': str,
        'firstName': str,
        'lastName': str,
        'mobile_phone': str,
        'telephone': str,
        'homeOffice': str,
        'workingOffice': str,
        'department': str,
        'departmentCode': str,
        'projectIds': [],
        'country': str,
        'role': str,
        'joinDate': str
    }

    def __init__(self):
        self.login = None
        self.email = None
        self.employeeNumber = None
        self.secondEmail = None
        self.firstName = None
        self.lastName = None
        self.mobile_phone = None
        self.telephone = None
        self.homeOffice = None
        self.workingOffice = None
        self.department = None
        self.departmentCode = None
        self.projectIds = None
        self.country = None
        self.role = None
        self.joinDate = None
