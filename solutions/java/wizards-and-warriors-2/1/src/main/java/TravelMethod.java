public enum TravelMethod {
    WALKING,
    HORSEBACK;

    @Override
    public String toString() {
        if (name() == "WALKING") {
            return "by " + name().toLowerCase();
        }
        return "on " + name().toLowerCase();
    }
}
