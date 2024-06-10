import { BrowserRouter, Routes, Route } from "react-router-dom";

import Main from "./components/Main/Main";
import Registration from "./components/Registration/Registration";
import Login from "./components/Login/Login";
import Profile from "./components/Profile/Profile";
import ProfileEdit from "./components/Profile/ProfileEdit/ProfileEdit";
import Events from "./components/Events/Events";
import Event from "./components/Events/Event/Event";

function App() {
  return (
    <>
      <BrowserRouter>
        <Routes>
          <Route path="/" element={<Main />} />
          <Route path="/main" element={<Main />} />
          <Route path="/login" element={<Login />} />
          <Route path="/registration" element={<Registration />} />
          <Route path="/profile" element={<Profile />} />
          <Route path="/profile-edit" element={<ProfileEdit />} />
          <Route path="/events" element={<Events />} />
          <Route path="/event" element={<Event />} />
        </Routes>
      </BrowserRouter>
    </>
  );
}

export default App;
