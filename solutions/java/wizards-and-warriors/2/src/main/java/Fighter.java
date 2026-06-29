class Fighter {

    boolean isVulnerable() {
        return true;
    }

    int getDamagePoints(Fighter fighter) {
        return 1;
    }
}

class Warrior extends Fighter {

    public String toString() {
        return "Fighter is a Warrior";
    }

    @Override
    public boolean isVulnerable() {
        return false;
    }

    @Override
    public int getDamagePoints(Fighter fighter) {
        if (fighter.isVulnerable()) {
            return 10;
        } else {
            return 6;
        }
    }
}

class Wizard extends Fighter {

    private boolean isPreparedSpell = false;

    public String toString() {
        return "Fighter is a Wizard";
    }

    public void prepareSpell() {
        isPreparedSpell = true;
    }

    @Override
    public boolean isVulnerable() {
        return !isPreparedSpell;
    }

    @Override
    public int getDamagePoints(Fighter fighter) {
        if (isPreparedSpell) return 12;
        return 3;
    }
}
