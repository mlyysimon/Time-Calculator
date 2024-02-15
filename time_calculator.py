def add_time(start, duration, day = 'False'):
  # List the days of the week
  day_of_week = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

  # Split time into hours, minutes, and AM/PM
  [start_hour, start_minute] = start.split(':')
  [start_minute, start_ampm] = start_minute.split(' ')

  [duration_hour, duration_minute] = duration.split(':')

  # Add minutes and hours together
  total_minute = int(start_minute) + int(duration_minute)
  total_hour = int(start_hour) + int(duration_hour)
  total_ampm = start_ampm
  next_day = 0

  # If the minutes are greater than 60, add the appropriate hours and get the remainder minutes
  if total_minute > 60:
    total_hour += total_minute // 60
    total_minute = total_minute % 60

  # Format the minutes after changing to integer
  if total_minute < 10:
    total_minute = f"0{total_minute}"

  # Adjust the AM PM if the total hours are greater than 12
  # Count how many days change
  if total_hour >= 12:
    ampm_change = total_hour // 12
    total_hour = total_hour % 12
    if total_hour == 0:
      total_hour = 12
    if ampm_change % 2 == 1:
      if start_ampm == 'AM':
        total_ampm = 'PM'
        next_day = ampm_change // 2
      else: # if start_ampm is PM
        total_ampm = 'AM'
        next_day = (ampm_change + 1) // 2
    else: 
      next_day = ampm_change // 2


  # Determine how many days have passed and what day of the week it is
  day_string = ''

  if day != 'False':
    day = day.lower()
    find_day = day_of_week.index(day)
    day_change = day_of_week[(find_day + next_day) % 7]
    day_string = ', ' + day_change.capitalize()
    if next_day == 1:
      day_string += ' (next day)'
    elif next_day > 1:
      day_string += ' (' + str(next_day) + ' days later)'
  else:
    if next_day == 1:
      day_string = ' (next day)'
    elif next_day > 1:
      day_string = ' (' + str(next_day) + ' days later)'

  new_time = f"{total_hour}:{total_minute} {total_ampm}{day_string}"

  return new_time