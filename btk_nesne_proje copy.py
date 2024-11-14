{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Product created: Laptop at 2024-11-14 11:53:59.385232\n",
      "Product(Name: Laptop, Price: 1500, Quantity: 3)\n",
      "Total Price: 4500\n",
      "Product created: Mouse at 2024-11-14 11:53:59.385725\n",
      "Product(Name: Mouse, Price: 20, Quantity: 10)\n",
      "Total Price: 200\n"
     ]
    }
   ],
   "source": [
    "from datetime import datetime\n",
    "\n",
    "class Product:\n",
    "    def __init__(self, name, price, quantity):\n",
    "        self.name = name\n",
    "        self.price = price\n",
    "        self.quantity = quantity\n",
    "        print(f\"Product created: {self.name} at {datetime.now()}\")\n",
    "\n",
    "    # Name encapsulation\n",
    "    @property\n",
    "    def name(self):\n",
    "        return self._name\n",
    "\n",
    "    @name.setter\n",
    "    def name(self, value):\n",
    "        if 3 <= len(value) <= 8:\n",
    "            self._name = value\n",
    "        else:\n",
    "            raise ValueError(\"Name must be between 3 and 8 characters\")\n",
    "\n",
    "    # Price encapsulation\n",
    "    @property\n",
    "    def price(self):\n",
    "        return self._price\n",
    "\n",
    "    @price.setter\n",
    "    def price(self, value):\n",
    "        if value >= 0:\n",
    "            self._price = value\n",
    "        else:\n",
    "            raise ValueError(\"Price must be at least 0\")\n",
    "\n",
    "    # Quantity encapsulation\n",
    "    @property\n",
    "    def quantity(self):\n",
    "        return self._quantity\n",
    "\n",
    "    @quantity.setter\n",
    "    def quantity(self, value):\n",
    "        if value >= 1:\n",
    "            self._quantity = value\n",
    "        else:\n",
    "            raise ValueError(\"Quantity must be at least 1\")\n",
    "\n",
    "    def get_total_price(self):\n",
    "        return self.price * self.quantity\n",
    "\n",
    "    def __str__(self):\n",
    "        return f\"Product(Name: {self.name}, Price: {self.price}, Quantity: {self.quantity})\"\n",
    "\n",
    "# Testing Product class\n",
    "product1 = Product(\"Laptop\", 1500, 3)\n",
    "print(product1)\n",
    "print(\"Total Price:\", product1.get_total_price())\n",
    "\n",
    "product2 = Product(\"Mouse\", 20, 10)\n",
    "print(product2)\n",
    "print(\"Total Price:\", product2.get_total_price())\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "ename": "FileNotFoundError",
     "evalue": "[Errno 2] No such file or directory: 'Products.txt'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mFileNotFoundError\u001b[0m                         Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[2], line 19\u001b[0m\n\u001b[0;32m     16\u001b[0m         \u001b[38;5;28;01mreturn\u001b[39;00m total_balance_with_vat\n\u001b[0;32m     18\u001b[0m \u001b[38;5;66;03m# Testing ProductHelper class\u001b[39;00m\n\u001b[1;32m---> 19\u001b[0m products \u001b[38;5;241m=\u001b[39m \u001b[43mProductHelper\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mcreate_item_from_text\u001b[49m\u001b[43m(\u001b[49m\u001b[38;5;124;43m'\u001b[39;49m\u001b[38;5;124;43mProducts.txt\u001b[39;49m\u001b[38;5;124;43m'\u001b[39;49m\u001b[43m)\u001b[49m\n\u001b[0;32m     20\u001b[0m \u001b[38;5;28;01mfor\u001b[39;00m product \u001b[38;5;129;01min\u001b[39;00m products:\n\u001b[0;32m     21\u001b[0m     \u001b[38;5;28mprint\u001b[39m(product)\n",
      "Cell \u001b[1;32mIn[2], line 6\u001b[0m, in \u001b[0;36mProductHelper.create_item_from_text\u001b[1;34m(file_path)\u001b[0m\n\u001b[0;32m      3\u001b[0m \u001b[38;5;129m@staticmethod\u001b[39m\n\u001b[0;32m      4\u001b[0m \u001b[38;5;28;01mdef\u001b[39;00m \u001b[38;5;21mcreate_item_from_text\u001b[39m(file_path):\n\u001b[0;32m      5\u001b[0m     products \u001b[38;5;241m=\u001b[39m []\n\u001b[1;32m----> 6\u001b[0m     \u001b[38;5;28;01mwith\u001b[39;00m \u001b[38;5;28;43mopen\u001b[39;49m\u001b[43m(\u001b[49m\u001b[43mfile_path\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[38;5;124;43m'\u001b[39;49m\u001b[38;5;124;43mr\u001b[39;49m\u001b[38;5;124;43m'\u001b[39;49m\u001b[43m)\u001b[49m \u001b[38;5;28;01mas\u001b[39;00m file:\n\u001b[0;32m      7\u001b[0m         \u001b[38;5;28;01mfor\u001b[39;00m line \u001b[38;5;129;01min\u001b[39;00m file:\n\u001b[0;32m      8\u001b[0m             name, price, quantity \u001b[38;5;241m=\u001b[39m line\u001b[38;5;241m.\u001b[39mstrip()\u001b[38;5;241m.\u001b[39msplit(\u001b[38;5;124m'\u001b[39m\u001b[38;5;124m,\u001b[39m\u001b[38;5;124m'\u001b[39m)\n",
      "File \u001b[1;32m~\\AppData\\Roaming\\Python\\Python313\\site-packages\\IPython\\core\\interactiveshell.py:324\u001b[0m, in \u001b[0;36m_modified_open\u001b[1;34m(file, *args, **kwargs)\u001b[0m\n\u001b[0;32m    317\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m file \u001b[38;5;129;01min\u001b[39;00m {\u001b[38;5;241m0\u001b[39m, \u001b[38;5;241m1\u001b[39m, \u001b[38;5;241m2\u001b[39m}:\n\u001b[0;32m    318\u001b[0m     \u001b[38;5;28;01mraise\u001b[39;00m \u001b[38;5;167;01mValueError\u001b[39;00m(\n\u001b[0;32m    319\u001b[0m         \u001b[38;5;124mf\u001b[39m\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mIPython won\u001b[39m\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mt let you open fd=\u001b[39m\u001b[38;5;132;01m{\u001b[39;00mfile\u001b[38;5;132;01m}\u001b[39;00m\u001b[38;5;124m by default \u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m    320\u001b[0m         \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mas it is likely to crash IPython. If you know what you are doing, \u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m    321\u001b[0m         \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124myou can use builtins\u001b[39m\u001b[38;5;124m'\u001b[39m\u001b[38;5;124m open.\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m    322\u001b[0m     )\n\u001b[1;32m--> 324\u001b[0m \u001b[38;5;28;01mreturn\u001b[39;00m \u001b[43mio_open\u001b[49m\u001b[43m(\u001b[49m\u001b[43mfile\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[38;5;241;43m*\u001b[39;49m\u001b[43margs\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[38;5;241;43m*\u001b[39;49m\u001b[38;5;241;43m*\u001b[39;49m\u001b[43mkwargs\u001b[49m\u001b[43m)\u001b[49m\n",
      "\u001b[1;31mFileNotFoundError\u001b[0m: [Errno 2] No such file or directory: 'Products.txt'"
     ]
    }
   ],
   "source": [
    "class ProductHelper:\n",
    "    \n",
    "    @staticmethod\n",
    "    def create_item_from_text(file_path):\n",
    "        products = []\n",
    "        with open(file_path, 'r') as file:\n",
    "            for line in file:\n",
    "                name, price, quantity = line.strip().split(',')\n",
    "                products.append(Product(name, float(price), int(quantity)))\n",
    "        return products\n",
    "    \n",
    "    @staticmethod\n",
    "    def get_total_balance(products):\n",
    "        total_balance = sum(p.get_total_price() for p in products)\n",
    "        total_balance_with_vat = total_balance * 1.20  # %20 KDV eklenmiş hali\n",
    "        return total_balance_with_vat\n",
    "\n",
    "# Testing ProductHelper class\n",
    "products = ProductHelper.create_item_from_text('Products.txt')\n",
    "for product in products:\n",
    "    print(product)\n",
    "\n",
    "print(\"Total Balance with VAT:\", ProductHelper.get_total_balance(products))\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
