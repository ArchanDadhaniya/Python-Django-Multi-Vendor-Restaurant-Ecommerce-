def detectUser(user):
    if user.role == 1:
        return 'vendorDashboard'
    elif user.role == 2:
        return 'customerDashboard'
    elif user.role is None and user.is_superadmin:
        redirectUrl = '/admin'
        return redirectUrl