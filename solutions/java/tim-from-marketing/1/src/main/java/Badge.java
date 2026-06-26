class Badge {
    public String print(Integer id, String name, String department) {
        StringBuilder sb = new StringBuilder();

        if (id != null) {
            sb.append(String.format("[%d] - ", id));
        }

        if (name != null) {
            sb.append(String.format("%s - ", name));
        }

        if (department != null) {
            sb.append(department.toUpperCase());
        } else {
            sb.append("OWNER");
        }

        return sb.toString();
    }
}
