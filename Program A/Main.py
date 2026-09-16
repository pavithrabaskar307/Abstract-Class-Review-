class Article {
    String title;
    int wordCount;

    Article(String title, int wordCount) {
        this.title = title;
        this.wordCount = wordCount;
    }

    void display() {
        System.out.println("Title: " + title);
        System.out.println("Word Count: " + wordCount);
    }
}

class FeatureArticle extends Article {
    String authorBio;

    FeatureArticle(String title, int wordCount, String authorBio) {
        super(title, wordCount);
        this.authorBio = authorBio;
    }

    @Override
    void display() {
        System.out.println("Feature Article Details");
        System.out.println("Title: " + title);
        System.out.println("Word Count: " + wordCount);
        System.out.println("Author Bio: " + authorBio);
    }
}

public class Main {
    public static void main(String[] args) {
        FeatureArticle article = new FeatureArticle(
            "Artificial Intelligence",
            1200,
            "AI Researcher"
        );

        article.display();
    }
}
