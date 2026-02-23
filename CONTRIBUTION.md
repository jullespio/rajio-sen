# ＣＯＮＴＲＩＢＵＴＩＯＮ ＧＵＩＤＥ (寄稿ガイド)

Welcome to the **Rajio-Sen (ラジオ船)** project! We're thrilled that you want to help keep the pirate frequency alive. Before you start hacking the signal, please review these directives.

## ＧＥＴＴＩＮＧ ＳＴＡＲＴＥＤ (準備)

Ensure your station is equipped with the following:
* **Git**: To track your modifications.
* **Python 3.6+**: The ship's primary core.
* **FFmpeg**: Essential for the sub-space audio relay.

## ＨＯＷ ＴＯ ＣＯＮＴＲＩＢＵＴＥ (貢献方法)

### １. Ｆｏｒｋ ｔｈｅ Ｒｅｐｏｓｉｔｏｒｙ
Click the **Fork** button on the top right of the [jullespio/rajio-sen](https://github.com/jullespio/rajio-sen) page.

### ２. Ｃｌｏｎｅ Ｙｏｕｒ Ｆｏｒｋ
```bash
git clone [https://github.com/YOUR_USERNAME/rajio-sen.git](https://github.com/YOUR_USERNAME/rajio-sen.git)
cd rajio-sen
git checkout -b feature/your-new-signal
```

### ３. Ｉｎｓｔａｌｌ Ｄｅｐｅｎｄｅｎｃｉｅｓ
For local development and testing, initialize a virtual environment and install the package in editable mode. This ensures all requirements are met and the rajio command is linked to your shell.
```bash
python -m venv venv
source venv/bin/activate  # Or venv\Scripts\activate on Windows
pip install -r requirements.txt
pip install -r requirements-dev.txt
```

### ４. Ｍａｋｅ Ｃｈａｎｇｅｓ
Modify the hull and engine room as required. Keep the code clean and follow the **minimalist/vaporwave aesthetic** guidelines established for the UI.

### ５. Ｔｅｓｔ Ｙｏｕｒ Ｃｈａｎｇｅｓ
Before pushing back to the mothership, ensure the signal is stable. Use the editable installation to test the `rajio` command:
```bash
pip install -e .
rajio --search "vaporwave"
```

### ６. Ｃｏｍｍｉｔ ＆ Ｐｕｓｈ
We follow a structured log format for ship's records.
```bash
git add .
git commit -s -m "feat(ui): Add new neon glow to the HUD"
git push origin feature/your-new-signal
```

### ７. Ｃｒｅａｔｅ ａ Ｐｕｌｌ Ｒｅｑｕｅｓｔ
Visit the repository on GitHub. Submit your transmission to the `jullespio/rajio-sen` repository. Provide a detailed description of your structural refit in the PR logs.

---

<div align=center>
<p align=center> ＯＦＦ－ＧＲＩＤ ＮＥＴＷＯＲＫ // ＰＩＲＡＴＥ ＲＡＤＩＯ ＳＹＮＤＩＣＡＴＥ </p>
</div>