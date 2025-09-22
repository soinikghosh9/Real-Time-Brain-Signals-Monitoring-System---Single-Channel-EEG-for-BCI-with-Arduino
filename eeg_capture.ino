#include "KickFiltersRT.h"

// Initialize KickFiltersRT for float data type
KickFiltersRT<float> filtersRT;

// Sample rate approximation (adjust based on actual rate)
const float fs = 256.0; // Adjust this value to match your actual sample rate
const float threshold = 0.6; // Adjust this value based on your signal characteristics

// Variables for heart rate peak detection
unsigned long lastPeakTime = 0;
unsigned long currentPeakTime = 0;
int peakCount = 0;

void setup() {
  // Initialize serial communication at 115200 bits per second:
  Serial.begin(115200);
}

void loop() {
  // Read the input on analog pin A0 for EEG:
  int eegSensorValue = analogRead(A0);

  // Apply highpass filter for EEG
  float eegHighpassed = filtersRT.highpass(eegSensorValue, 1, fs);
  
  // Apply lowpass filter on the result of highpass filter for EEG
  float eegBandpassed = filtersRT.lowpass(eegHighpassed, 40.0, fs);

  // Read the input on analog pin A1 for heart rate:
  int heartRateSensorValue = analogRead(A1);

  // Apply highpass filter for heart rate
  float heartRateHighpassed = filtersRT.highpass(heartRateSensorValue, 0.5, fs);
  
  // Apply lowpass filter on the result of highpass filter for heart rate
  float heartRateBandpassed = filtersRT.lowpass(heartRateHighpassed, 2.5, fs);

  // Print out the filtered EEG value:
  //Serial.print("EEG: ");
  Serial.println(eegBandpassed);

  // Print out the filtered heart rate value:
  //Serial.print("Heart Rate: ");
  Serial.println(heartRateBandpassed);

  // Peak detection for heart rate
  if (heartRateBandpassed > threshold) {
    currentPeakTime = millis();
    if (currentPeakTime - lastPeakTime > 300) { // Minimum interval to avoid false peaks (300ms corresponds to 200 BPM)
      lastPeakTime = currentPeakTime;
      peakCount++;
    }
  }

  // Calculate and print heart rate in BPM every 5 seconds
  if (millis() - currentPeakTime >= 5000) {
    float bpm = (peakCount * 60.0) / 5.0; // BPM calculation
    Serial.print("BPM: ");
    Serial.println(bpm);
    peakCount = 0;
    currentPeakTime = millis();
  }

  // About 256Hz sample rate (adjust delay if needed)
  delayMicroseconds(3900);
}
