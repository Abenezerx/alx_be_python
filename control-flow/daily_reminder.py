task = input('Enter your task:')
priority = input('Priorty (high/medium/low):')
time_bound = input('Is it time bound? (Yes/ No):')

reminder=''

match priority:
    case 'high':
        reminder = f'Reminder: {task} is a high priority task.'
    case 'medium':
        reminder = f'Reminder: {task} is a medium priority task.'
    case 'low':
        reminder = f'Reminder: {task} is a low priority task.'
    case _:
        reminder = f'Reminder: {task} (Priority: Unknown)'
        print("Invalid priority entered. Please use 'high', 'medium', or 'low'.")
if time_bound == 'yes':
    reminder += ' that requires immediate attention today!'
elif time_bound == 'no' and priority == 'high':
    reminder += ' since it is not time bound, do not be negligent'
else:
    reminder += ' Consider completing it when you have free time.'

print('reminder')