class VacuumCleaner:
    def __init__(self):
       
        self.rooms = {
            "A": "Dirty",
            "B": "Dirty"
        }
        self.position = "A"

    def display_state(self):
        print("\nCurrent State:")
        print("Room A:", self.rooms["A"])
        print("Room B:", self.rooms["B"])
        print("Vacuum Position:", self.position)

    def clean(self):
        print(f"Action: CLEAN room {self.position}")
        self.rooms[self.position] = "Clean"

    def move_right(self):
        if self.position == "A":
            self.position = "B"
            print("Action: MOVE RIGHT")

    def move_left(self):
        if self.position == "B":
            self.position = "A"
            print("Action: MOVE LEFT")

    def run(self):
        print("=== AI VACUUM CLEANER ===")

        while "Dirty" in self.rooms.values():
            self.display_state()

            if self.rooms[self.position] == "Dirty":
                self.clean()

            elif self.position == "A":
                self.move_right()

            elif self.position == "B":
                self.move_left()

        self.display_state()
        print("\nAll rooms are CLEAN.")
        print("Goal achieved!")

vacuum = VacuumCleaner()

vacuum.run()
