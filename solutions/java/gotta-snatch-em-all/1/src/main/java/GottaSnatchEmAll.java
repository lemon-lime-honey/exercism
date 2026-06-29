import java.util.List;
import java.util.Set;
import java.util.HashSet;

class GottaSnatchEmAll {

    static Set<String> cardSet = new HashSet<>();

    static Set<String> newCollection(List<String> cards) {
        cardSet.clear();

        for (String card : cards) {
            cardSet.add(card);
        }

        return cardSet;
    }

    static boolean addCard(String card, Set<String> collection) {
        if (collection.contains(card)) return false;
        collection.add(card);
        return true;
    }

    static boolean canTrade(Set<String> myCollection, Set<String> theirCollection) {
        Set<String> mySub = new HashSet<>(myCollection);
        Set<String> theirSub = new HashSet<>(theirCollection);

        mySub.removeAll(theirCollection);
        theirSub.removeAll(myCollection);

        return !mySub.isEmpty() && !theirSub.isEmpty();
    }

    static Set<String> commonCards(List<Set<String>> collections) {
        Set<String> result = new HashSet<>(collections.get(0));

        for (int i = 1; i < collections.size(); i++) {
            result.retainAll(collections.get(i));
        }

        return result;
    }

    static Set<String> allCards(List<Set<String>> collections) {
        Set<String> result = new HashSet<>(collections.get(0));

        for (int i = 1; i < collections.size(); i++) {
            result.addAll(collections.get(i));
        }

        return result;
    }
}
