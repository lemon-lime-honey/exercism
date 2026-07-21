// Package weather "description".
package weather

var (
    // CurrentCondition "description".
	CurrentCondition string
    // CurrentLocation "description".
	CurrentLocation  string
)

// Forecast "description".
func Forecast(city, condition string) string {
	CurrentLocation, CurrentCondition = city, condition
	return CurrentLocation + " - current weather condition: " + CurrentCondition
}
