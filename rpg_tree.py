class StoryNode:
    """Represents a node in the decision tree."""
    def __init__(self, event_number, description, left=None, right=None):
        self.event_number = event_number
        self.description = description
        self.left = left  # left child node
        self.right = right  # right child node

class GameDecisionTree:
    """Binary decision tree for the RPG."""
    def __init__(self):
        self.nodes = {}
        self.root = None

    def insert(self, event_number, description, left_event, right_event):
        """Insert a new story node into the tree."""
        node = self.nodes.get(event_number, StoryNode(event_number, description))
        node.description = description  # Update description if it was previously "Undecided path"

        if left_event is not None:
            if left_event not in self.nodes:
                self.nodes[left_event] = StoryNode(left_event,"")
            node.left = self.nodes[left_event]

        if right_event is not None:
            if right_event not in self.nodes:
                self.nodes[right_event] = StoryNode(right_event,"")
            node.right = self.nodes[right_event]

        self.nodes[event_number] = node  # Store node
        if not self.root:
            self.root = node  # Set root to the first inserted node

    def play_game(self):
        """Interactive function that plays the RPG."""
        current = self.root
        while current:
            print("\n" + current.description)
            if not current.left and not current.right:
                break

            choice = input("Choose 1 or 2: ").strip().lower()
            if choice == "1" and current.left:
                current = current.left
            elif choice == "2" and current.right:
                current = current.right
            else:
                print("Invalid choice, try again.")

def load_story(filename, game_tree):
    """Load story from a file and construct the decision tree."""
    try:
        with open(filename, "r") as file:
            for line in file:
                event_number, description, left_event, right_event = line.strip().split("|")
                game_tree.insert(
                    int(event_number),
                    description.strip(),
                    int(left_event) if left_event != "-1" else None,
                    int(right_event) if right_event != "-1" else None
                )
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")


# Main program
if __name__ == "__main__":
    game_tree = GameDecisionTree()
    load_story("story.txt", game_tree)
    game_tree.play_game()
