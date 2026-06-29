import java.util.Map;
import java.util.HashMap;

public class DialingCodes {

    private Map<Integer, String> codeMap = new HashMap<Integer, String>();

    public Map<Integer, String> getCodes() {
        return codeMap;
    }

    public void setDialingCode(Integer code, String country) {
        codeMap.put(code, country);
    }

    public String getCountry(Integer code) {
        return codeMap.get(code);
    }

    public void addNewDialingCode(Integer code, String country) {
        if (!codeMap.containsKey(code) && !codeMap.containsValue(country)) {
            codeMap.put(code, country);
        }
    }

    public Integer findDialingCode(String country) {
        Integer result = null;

        for (Map.Entry<Integer, String> entry : codeMap.entrySet()) {
            if (entry.getValue() == country) {
                result = entry.getKey();
            }
        }

        return result;
    }

    public void updateCountryDialingCode(Integer code, String country) {
        if (!codeMap.containsValue(country)) return;

        for (Map.Entry<Integer, String> entry : codeMap.entrySet()) {
            if (entry.getValue() == country) {
                codeMap.remove(entry.getKey());
                codeMap.put(code, country);
            }
        }
    }
}
