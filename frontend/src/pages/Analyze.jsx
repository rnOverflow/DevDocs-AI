import { useState } from "react";
import { useNavigate } from "react-router-dom";

export default function Analyze() {
    const [input, setInput] = useState("");
    const [loading, setLoading] = useState(false);

    const navigate = useNavigate();

    const handleAnalyze = () => {
        if (!input.trim()) return;

        setLoading(true);

        setTimeout(() => {
            navigate("/result", { state: input });
        }, 2000);
    };

    return (
        <div
            style={{
                minHeight: "100vh",
                display: "flex",
                justifyContent: "center",
                alignItems: "center",
            }}
        >
            <div
                style={{
                    width: "100%",
                    maxWidth: "800px",
                    padding: "30px",
                    background: "#020617",
                    borderRadius: "12px",
                    boxShadow: "0 0 20px rgba(0,0,0,0.3)",
                }}
            >
                <h1 style={{ textAlign: "center" }}>
                    DevDocs AI 🚀
                </h1>

                <p style={{ textAlign: "center", marginTop: "10px" }}>
                    Paste your code or documentation
                </p>

                <textarea
                    placeholder="Paste your code here..."
                    value={input}
                    onChange={(e) => setInput(e.target.value)}
                    rows={10}
                    style={{
                        width: "100%",
                        marginTop: "20px",
                        padding: "12px",
                    }}
                />

                <button
                    onClick={handleAnalyze}
                    disabled={loading}
                    style={{
                        marginTop: "20px",
                        width: "100%",
                        opacity: loading ? 0.6 : 1,
                    }}
                >
                    {loading ? "Analyzing..." : "Analyze"}
                </button>
            </div>
        </div>
    );
}