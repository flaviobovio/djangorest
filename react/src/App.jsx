import { BrowserRouter, Routes, Route } from "react-router-dom"
import { Navigator } from "./components/Navigator"
import { SwimmerPage } from "./pages/SwimmerPage"
import { SwimmerFormPage } from "./pages/SwimmerFormPage"

function App() {
  return (
    <BrowserRouter>
      <Navigator />
      <Routes>
        <Route path="/swimmer" element={<SwimmerPage />} />
        <Route path="/swimmerform" element={<SwimmerFormPage />} />
      </Routes>
    </BrowserRouter>
  )
}

export default App


