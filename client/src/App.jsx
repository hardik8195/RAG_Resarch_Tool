import "./App.css"
import Main from "./components/main/Main"
import Menubar from "./components/menubar/Menubar"
function App() {

  return (
    <>
      <div className="container">
        <div className="navbar">
          <h1>NEWS RESEARCH TOOL</h1>
        </div>
        <div className="content">
          <div className="menubar"><Menubar /></div>
          <div className="main-page"><Main /></div>
        </div>
      </div>
    </>
  )
}

export default App
