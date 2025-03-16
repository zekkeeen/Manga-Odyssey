import React, { useEffect, useState } from "react";
import axios from "axios";

function App() {
    const [message, setMessage] = useState("");

    useEffect(() => {
        axios.get("http://127.0.0.1:8000/api/hello/") // Django API URL
            .then(response => {
                setMessage(response.data.message);
            })
            .catch(error => console.error("Error fetching data:", error));
    }, []);

    return (
        <div>
            <h1>Manga Odysseys</h1>
            <p>{message}</p>
        </div>
    );
}

export default App;
