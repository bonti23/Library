The Library Application is designed to manage book rentals efficiently. It features two primary classes:
Client – Represents a library member who can borrow books. The system allows adding, updating, deleting, and displaying client records.
Book – Represents a book available in the library. Users can add, modify, remove, and view book details.
To facilitate the borrowing and returning process, the RentalRepository class acts as an intermediary, enabling clients to rent and return books seamlessly. This repository ensures proper tracking of borrowed books, prevents double rentals of the same copy, and maintains a structured rental history.
The undo operation is essential for ensuring that accidental modifications, deletions, or rentals can be reversed, maintaining data integrity. It allows users to revert the most recent actions, restoring the system to a previous state.
