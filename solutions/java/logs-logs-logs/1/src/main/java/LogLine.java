public class LogLine {

    private LogLevel level;
    private String shortStr;

    public LogLine(String logLine) {
        String target = logLine.substring(1,4);
        switch (target) {
            case "TRC":
                level = LogLevel.TRACE;
                break;
            case "DBG":
                level = LogLevel.DEBUG;
                break;
            case "INF":
                level = LogLevel.INFO;
                break;
            case "WRN":
                level = LogLevel.WARNING;
                break;
            case "ERR":
                level = LogLevel.ERROR;
                break;
            case "FTL":
                level = LogLevel.FATAL;
                break;
            default:
                level = LogLevel.UNKNOWN;
                break;
        }

        shortStr = level.getNum() + ":" + logLine.substring(7, logLine.length());
    }

    public LogLevel getLogLevel() {
        return level;
    }

    public String getOutputForShortLog() {
        return shortStr;
    }
}
