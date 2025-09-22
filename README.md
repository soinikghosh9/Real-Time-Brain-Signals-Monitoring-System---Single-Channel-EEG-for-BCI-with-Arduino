# Real-Time Brain Signals Monitoring System - Single Channel EEG for BCI with Arduino

<img width="1235" height="778" alt="Screenshot 2025-09-22 205154" src="https://github.com/user-attachments/assets/1f35e15f-56ca-4311-b039-f9d1a8498298" />

Paper Link: https://ieeexplore.ieee.org/abstract/document/10868917

**Short description**  
This repository contains code, firmware, and documentation for the project described in:  
S. Ghosh et al., *“Real-Time Brain Signals Monitoring System Using Single-Channel EEG for BCI Applications”*, AKGEC 2024. DOI: `10.1109/AKGEC62572.2024.10868917`.

The project demonstrates a low-power, wearable single-channel EEG acquisition system that performs real-time signal processing on an embedded microcontroller, visualizes signals in a GUI, and trains a lightweight deep learning model for classification of Eyes Open / Eyes Closed / Motor Imagery (hand open/close). Target applications include cognitive monitoring and simple BCI control (e.g., prosthetic arm control) with an emphasis on edge, green, and cost-effective deployment.

---

## Highlights
- Wearable single-channel EEG acquisition with a custom data-collection protocol.  
- Real-time edge processing on microcontroller (feature extraction + streaming).  
- GUI for live visualization, annotation, and dataset management.  
- Deep learning model trained on labeled conditions (eyes open, eyes closed, motor imagery) for event classification.  
- Low-power, low-cost, sustainable design suitable for prototyping BCIs and prosthetic control.


## Firmware / MCU

Firmware folder contains example code for streaming ADC readings and basic on-MCU feature extraction (e.g., moving average, bandpass filter).

Target platforms: low-power MCUs such as ESP32 / STM32 / Arduino Nano 33 BLE. Use the provided PlatformIO/Arduino sketches in /hardware/firmware/.

Ensure sampling rate, ADC gain, and anti-alias filtering match the configs/preprocess.yaml settings.

## Model & Edge Deployment

Focus on small models (≤1–5 MB) or use model quantization (8-bit) for MCU/edge accelerators (e.g., TensorFlow Lite, TinyML).

## Tools & tips:

Export PyTorch → ONNX → TFLite or use torch.quantization.

Profile inference latency on target hardware before clinical testing.

Save model config and normalization params together with checkpoints.

## Evaluation & Metrics

Classification metrics: Accuracy, Precision, Recall, F1, and confusion matrices for the three classes.

Robustness: cross-validation across sessions and subjects; report subject-wise performance to quantify generalization.

Runtime: streaming latency, CPU/memory usage, and power consumption on the target device.

## Data & Ethics

Use only consented and de-identified participant data. Include IRB/consent documentation in /docs/ if applicable.

Record and share minimal metadata: age range, handedness, session conditions (eyes open/closed, motor imagery instructions), sampling rate, electrode placement.

Follow local laws and institutional policies for human-subject research and data sharing.



## Dependencies (example)

- Python 3.8+

- numpy, scipy, pandas

- mne (optional, for EEG utilities)

- PyTorch or TensorFlow (model training)

- pyserial (serial communication with MCU)

- matplotlib / plotly (visualization)

- tkinter / PyQt / Dash (GUI)


## Citation

If you use this code or reproduce results, please cite:

S. Ghosh, C. Parikshith, F. Yashmeen, A. K. Srivastava, S. Sharma and N. Sharma,
"Real-Time Brain Signals Monitoring System Using Single-Channel EEG for BCI Applications,"
2024 2nd International Conference on Advancements and Key Challenges in Green Energy and Computing (AKGEC), pp.1–6, 2024.
DOI: 10.1109/AKGEC62572.2024.10868917
