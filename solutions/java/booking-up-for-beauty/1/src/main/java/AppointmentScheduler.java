import java.time.LocalDate;
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;
import java.time.format.TextStyle;
import java.util.Locale;

class AppointmentScheduler {
    public LocalDateTime schedule(String appointmentDateDescription) {
        DateTimeFormatter formatter = DateTimeFormatter.ofPattern("MM/dd/yyyy HH:mm:ss");
        return LocalDateTime.parse(appointmentDateDescription, formatter);
    }

    public boolean hasPassed(LocalDateTime appointmentDate) {
        return appointmentDate.isBefore(LocalDateTime.now());
    }

    public boolean isAfternoonAppointment(LocalDateTime appointmentDate) {
        int check = appointmentDate.getHour();
        return check >= 12 && check < 18;
    }

    public String getDescription(LocalDateTime appointmentDate) {
        StringBuilder sb = new StringBuilder();
        DateTimeFormatter date = DateTimeFormatter.ofPattern("EEEE, MMMM d, yyyy", Locale.ENGLISH);
        DateTimeFormatter time = DateTimeFormatter.ofPattern("h:mm a.", Locale.ENGLISH);
        sb.append("You have an appointment on ");
        sb.append(appointmentDate.format(date));
        sb.append(", at ");
        sb.append(appointmentDate.format(time));
        return sb.toString();
    }

    public LocalDate getAnniversaryDate() {
        return LocalDate.of(LocalDate.now().getYear(), 9, 15);
    }
}
