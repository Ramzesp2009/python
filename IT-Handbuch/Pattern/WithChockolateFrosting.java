public class WithChockolateFrosting extends CookieDecorator {
    public WithChockolateFrosting(Cookie cookie) {
        super(cookie);
    }

    @Override
    public double getPrice() {
        return super.getPrice() + 0.5;
    }

    @Override
    public String getIngredients() {
        return super.getIngredients() + ", Chockolate";
    }
}
