abstract class Review {
    abstract void publishReview();
}

class EditorReview extends Review {
    @Override
    void publishReview() {
        System.out.println(
            "Editor Review: Article approved for publishing."
        );
    }
}

public class Main {
    public static void main(String[] args) {
        EditorReview review = new EditorReview();
        review.publishReview();
    }
}
