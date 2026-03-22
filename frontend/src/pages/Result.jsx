import { useLocation, useNavigate } from "react-router-dom";
import { useEffect, useState } from "react";

export default function Result() {
    const location = useLocation();
    const navigate = useNavigate();

    const data = location.state;

    const [output, setOutput] = useState("");

    useEffect(() => {
        if (data) {
            setTimeout(() => {
                setOutput(
                    "✅ Code looks clean.\n\n🔍 Suggestions:\n- Improve variable naming\n- Add comments\n- Optimize loops\n\n🚀 Overall: Good structure!"
                );
            }, 1500);
        }
    }, [data]);

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
                }}
            >
                <h1 style={{ textAlign: "center" }}>Result</h1>

                {data ? (
                    <>
                        <h3 style={{ marginTop: "20px" }}>Input</h3>

                        <pre
                            style={{
                                background: "#111",
                                padding: "15px",
                                borderRadius: "8px",
                            }}
                        >
                            {data}
                        </pre>

                        <h3 style={{ marginTop: "20px" }}>
                            Generated Output
                        </h3>

                        {output ? (
                            <pre
                                style={{
                                    background: "#111",
                                    padding: "15px",
                                    borderRadius: "8px",
                                    whiteSpace: "pre-wrap",
                                }}
                            >
                                {output}
                            </pre>
                        ) : (
                            <p>Analyzing...</p>
                        )}

                        <button
                            onClick={() => navigate("/analyze")}
                            style={{
                                marginTop: "20px",
                                width: "100%",
                            }}
                        >
                            Go Back
                        </button>
                    </>
                ) : (
                    <p>No data received.</p>
                )}
            </div>
        </div>
    );
}