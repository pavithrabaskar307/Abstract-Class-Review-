class InvalidWordCountException extends Exception {
    public InvalidWordCountException(String message) {
        super(message);
    }
}

class Article {
    String title;
    int wordCount;

    Article(String title, int wordCount)
            throws InvalidWordCountException {

        if (wordCount <= 0) {
            throw new InvalidWordCountException(
                "Word count must be greater than zero."
            );
        }

        this.title = title;
        this.wordCount = wordCount;
    }

    void display() {
        System.out.println("Title: " + title);
        System.out.println("Word Count: " + wordCount);
    }
}

public class Main {
    public static void main(String[] args) {
        try {
            Article article = new Article(
                "Invalid Article", 0
            );

            article.display();

        } catch (InvalidWordCountException e) {
            System.out.println("Exception: " + e.getMessage());
        }
    }
}
