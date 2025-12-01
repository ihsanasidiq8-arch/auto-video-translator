import express from "express";
import multer from "multer";
import { exec } from "child_process";

const app = express();
const upload = multer({ dest: "uploads/" });

app.post("/upload", upload.single("video"), (req, res) => {
    const input = req.file.path;
    const output = "output_" + Date.now() + ".mp4";

    // Dummy: proses video (ubah ke perintah ffmpeg + whisper sesuai kebutuhan)
    exec(`cp ${input} ${output}`, () => {
        res.download(output);
    });
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => console.log(`Server running on port ${PORT}`));
