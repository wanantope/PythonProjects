buildings = {
    'skyscrapers': {
        'SuperOffice': {
            'floors': 120,
            'workers': 1000,
        },
    },
    'houses': {
        'John`s house': {
            'floors': 3,
            'livers': 7,
            'cars': 3,
            'address': 'Super street, 103, C',
        },
        'Bob`s house': {
            'floors': 3,
            'livers': 4,
            'cars': 1,
            'address': 'Sigma street, 22, B',
        },
    },
    'schools': {
        'Sigma School': {
            'floors': 3,
            'workers': 75,
            'students': 260,
        },
    },
}


def is_same_street(address1: dict, address2: dict) -> bool:
    return address1 == address2


same = is_same_street(buildings['houses']['John`s house'], buildings['houses']['Bob`s house'])

print(same)
