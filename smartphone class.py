class Smartphone:
    """A class representing a smartphone with various features."""
    
    def __init__(self, brand, model, storage, os):
        """Initialize smartphone attributes"""
        self.brand = brand
        self.model = model
        self.storage = storage  # in GB
        self.os = os  # operating system
        self.battery = 100  # percentage
        self.is_locked = True
        
    def unlock(self, pin):
        """Unlock the phone with a PIN"""
        if pin == "1234":  # simple PIN for demonstration
            self.is_locked = False
            print("Phone unlocked!")
        else:
            print("Wrong PIN!")
    
    def install_app(self, app_name):
        """Install an application if phone is unlocked"""
        if not self.is_locked:
            print(f"Installing {app_name}...")
            return True
        print("Cannot install app - phone is locked!")
        return False
    
    def use_battery(self, amount):
        """Reduce battery level by specified amount"""
        self.battery = max(0, self.battery - amount)
        if self.battery < 20:
            print("Low battery warning!")
    
    def charge(self):
        """Charge the battery to 100%"""
        self.battery = 100
        print("Battery fully charged!")
    
    def __str__(self):
        """String representation of the smartphone"""
        return f"{self.brand} {self.model} ({self.storage}GB, {self.os})"


# Inheritance example: PremiumSmartphone extends Smartphone
class PremiumSmartphone(Smartphone):
    """A premium smartphone with additional features"""
    
    def __init__(self, brand, model, storage, os, has_stylus, waterproof):
        """Initialize with additional premium features"""
        super().__init__(brand, model, storage, os)
        self.has_stylus = has_stylus
        self.waterproof = waterproof
    
    def use_stylus(self):
        """Use the stylus if available"""
        if self.has_stylus:
            print("Using stylus for precise input...")
        else:
            print("No stylus available on this device")
    
    def take_underwater_photo(self):
        """Take photo underwater if phone is waterproof"""
        if self.waterproof:
            print("Taking amazing underwater photo!")
        else:
            print("Cannot take underwater photo - phone not waterproof!")


# Example usage:
# my_phone = Smartphone("Apple", "iPhone 15", 256, "iOS")
# my_phone.unlock("1234")
# my_phone.install_app("Instagram")
# print(my_phone)

# premium_phone = PremiumSmartphone("Samsung", "Galaxy Note", 512, "Android", True, True)
# premium_phone.use_stylus()
# premium_phone.take_underwater_photo()