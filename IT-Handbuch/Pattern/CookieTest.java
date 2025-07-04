public class CookieTest {
    public static void cookieInfo(Cookie cookie) {
        System.out.println("Zutaten: " + cookie.getIngredients());
        System.out.println("Preis:   " + cookie.getPrice() + "\n");
    }

    public static void main(String[] args) {
        Cookie cookie = new PlainCookie();
        cookieInfo(cookie);
        cookie = new WithChockolateFrosting(cookie);
        cookieInfo(cookie);
        cookie = new WithSprinkles(cookie, "Zucker");
        cookieInfo(cookie);
        Cookie cookie2 = new WithChockolateFrosting(new WithSprinkles(new PlainCookie(), "Schoko"));
        cookieInfo(cookie2);
    }
}
