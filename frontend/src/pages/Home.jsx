import { useNavigate } from "react-router-dom";

export default function Home() {
    const navigate = useNavigate();

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
                    textAlign: "center",
                    background: "#020617",
                    padding: "40px",
                    borderRadius: "12px",
                    width: "400px",
                }}
            >
                <h1>DevDocs AI 🚀</h1>

                <p style={{ marginTop: "10px" }}>
                    Analyze your code instantly
                </p>

                <button
                    onClick={() => navigate("/analyze")}
                    style={{
                        marginTop: "20px",
                        width: "100%",
                    }}
                >
                    Start Analyzing
                </button>
            </div>
        </div>
    );
}