from state import State
from state_machine import StateMachine


def main():
    digits = list('0123456789')

    ############ Общая часть
    end_state = State('end_state', [])

    general10 = State('general10', [
        (digits, end_state)
    ])

    general9 = State('general9', [
        (digits, general10)
    ])

    general8 = State('general8', [
        (digits, general9)
    ])

    general7 = State('general7', [
        (digits, general8)
    ])

    general_tire2 = State('general_tire2', [
        (['-'], general7)
    ])

    general6 = State('general6', [
        (digits, general_tire2)
    ])

    general5 = State('general5', [
        (digits, general6)
    ])

    general4 = State('general4', [
        (digits, general5)
    ])

    general3 = State('general3', [
        (digits, general4)
    ])

    general_tire1 = State('general_tire1', [
        (['-'], general3)
    ])

    general2 = State('general2', [
        (digits, general_tire1)
    ])

    general1 = State('general', [
        (digits, general2)
    ])

    ###############

    mir_sber4 = State('mir_sber4', [
        (['4'], general1)
    ], message='Сбербанк')

    mir_sber2 = State('mir_sber2', [
        (['2'], mir_sber4)
    ])

    mir_tire = State('mir_tire', [
        (['-'], mir_sber2)
    ])

    mir_sber3 = State('mir_sber3', [
        (['3'], mir_tire)
    ])

    mir_sber = State('mir_sber', [
        (['4'], mir_sber3)
    ])
##################
    mir_tenek2 = State('mir_tenek2', [
        (['2'], general1)
    ], message='Тенек')

    mir_tenek6 = State('mir_tenek6', [
        (['6'], mir_tenek2)
    ])

    mir_tire2 = State('mir_tire2', [
        (['-'], mir_tenek6)
    ])

    mir_tenek7 = State('mir_tenek7', [
        (['7'], mir_tire2)
    ])

    mir_tenek = State('mir_tenek', [
        (['6'], mir_tenek7)
    ])
##############
    mir_vabank0 = State('mir_vabank0', [
        (['0'], general1)
    ], message='Вабанк')

    mir_vabank9 = State('mir_vabank9', [
        (['9'], mir_vabank0)
    ])

    mir_tire3 = State('mir_tire3', [
        (['-'], mir_vabank9)
    ])

    mir_vabank3 = State('mir_vabank3', [
        (['3'], mir_tire3)
    ])

    mir_vabank = State('mir_vabank', [
        (['7'], mir_vabank3)
    ])

    mir = State('mir', [
        (['3'], mir_sber),
        (['5'], mir_tenek),
        (['9'], mir_vabank)
    ], message='Мир ')
    
    ############################################################

    visa_tenek2 = State('visa_tenek2', [
        (['2'], general1)
    ], message='Тенек')

    visa_tenek6 = State('visa_tenek6', [
        (['6'], visa_tenek2)
    ])

    visa_tire2 = State('visa_tire2', [
        (['-'], visa_tenek6)
    ])

    visa_tenek7 = State('visa_tenek7', [
        (['7'], visa_tire2)
    ])

    visa_tenek = State('visa_tenek', [
        (['6'], visa_tenek7)
    ])
##################
    
    visa_vabank0 = State('visa_vabank0', [
        (['0'], general1)
    ], message='Вабанк')

    visa_vabank9 = State('visa_vabank9', [
        (['9'], visa_vabank0)
    ])

    visa_tire3 = State('visa_tire3', [
        (['-'], visa_vabank9)
    ])

    visa_vabank3 = State('visa_vabank3', [
        (['3'], visa_tire3)
    ])

    visa_vabank = State('visa_vabank', [
        (['7'], visa_vabank3)
    ])
    
    visa = State('visa', [
        (['5'], visa_tenek),
        (['9'], visa_vabank)
    ], message='Виза ')
    
    ######################################################

    master_vabank0 = State('master_vabank0', [
        (['0'], general1)
    ], message='Вабанк')

    master_vabank9 = State('master_vabank9', [
        (['9'], master_vabank0)
    ])

    master_tire3 = State('master_tire3', [
        (['-'], master_vabank9)
    ])

    master_vabank3 = State('master_vabank3', [
        (['3'], master_tire3)
    ])

    master_vabank = State('master_vabank', [
        (['7'], master_vabank3)
    ])
    
#######################
    

    master_sber4 = State('master_sber4', [
        (['4'], general1)
    ], message='Сбербанк')

    master_sber2 = State('master_sber2', [
        (['2'], master_sber4)
    ])

    master_tire = State('master_tire', [
        (['-'], master_sber2)
    ])

    master_sber3 = State('master_sber3', [
        (['3'], master_tire)
    ])

    master_sber = State('master_sber', [
        (['4'], master_sber3)
    ])

    master = State('master', [
        (['3'], master_sber),
        (['9'], master_vabank)
    ], message='Мастеркард ')

##################

    start_state = State('q0', [
        (['2'], mir),
        (['4'], visa),
        (['5'], master)
    ])

    ############# 2343-2486-4842-8964

    # input_str = input('Введите номер карты: ')
    # print(f"\nНомер карты {'корректный' if state_machine.test(input_str) else 'некорректный'}")

    test_strings = [
        '',
        '2343-2486-4842-8964',
        '5343-2486-4842-8964',
        '2567-6286-4842-8964',
        '4567-6286-4842-8964',
        '4973-9086-4842-8964',
        '2973-9086-4842-8964',
        '5973-9086-4842-8964',

        '4343-2486-4842-8964',
        '6973-9086-4842-8964',
    ]

    for test_string in test_strings:
        print(test_string + ":")
        try:
            state_machine = StateMachine(start_state, end_state)
            print(f"\nНомер карты {'корректный' if state_machine.test(test_string) else 'некорректный'}")
        except Exception as e:
            print(f'{e}')
        print()


if __name__ == '__main__':
    main()
