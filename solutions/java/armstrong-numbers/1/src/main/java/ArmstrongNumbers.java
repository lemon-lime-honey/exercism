class ArmstrongNumbers {

    boolean isArmstrongNumber(int numberToCheck) {
        int length = String.valueOf(numberToCheck).length();
        int ref = numberToCheck;
        int target = 0;

        while (ref != 0) {
            int num = ref % 10;
            target += Math.pow(num, length);
            ref /= 10;
        }

        return target == numberToCheck;
    }

}
