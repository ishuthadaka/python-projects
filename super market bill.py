import datetime

def generate_bill(items):
    """Generates a simple supermarket bill."""

    now = datetime.datetime.now()
    date_time = now.strftime("%Y-%m-%d %H:%M:%S")

    bill = f"""
    Supermarket Bill

    Date: {date_time}

    Items:
    """

    total_amount = 0
    for item, (quantity, price) in items.items():
        item_total = quantity * price
        bill += f"{item} - {quantity} x ${price:.2f} = ${item_total:.2f}\n"  # Basic formatting
        total_amount += item_total

    bill += f"\nTotal: ${total_amount:.2f}"

    return bill

def get_items():
  """Gets item details from the user (basic version)."""
  items = {}
  while True:
      item = input("Enter item name (or 'done'): ")
      if item.lower() == 'done':
          break
      try:
          quantity = int(input("Enter quantity: "))
          price = float(input("Enter price: "))
          items[item] = (quantity, price)  # Store as a tuple
      except ValueError:
          print("Invalid input. Please enter numbers for quantity and price.")
          continue # Ask again for the same item

  return items


if __name__ == "__main__":
    items = get_items()
    if items:
        bill = generate_bill(items)
        print(bill)
    else:
        print("No items entered.")