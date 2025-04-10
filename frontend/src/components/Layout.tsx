import { Outlet, Link, useNavigate } from 'react-router-dom';
import { Wallet, LogOut } from 'lucide-react';
import { useAuth } from '../context/AuthContext';

export function Layout() {
  const { userId, logout } = useAuth();
  const navigate = useNavigate();

  const handleLogout = () => {
    logout();
    navigate('/login');
  };

  return (
    <div className="min-h-screen bg-gray-50">
      <nav className="bg-white shadow-sm">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex justify-between h-16">
            <div className="flex items-center">
              <Wallet className="h-8 w-8 text-indigo-600" />
              <span className="ml-2 text-xl font-semibold text-gray-900">Budget Tracker</span>
            </div>
            <div className="flex items-center space-x-4">
              {userId ? (
                <>
                  <Link to="/dashboard" className="text-gray-700 hover:text-indigo-600">Dashboard</Link>
                  <Link to="/add-entry" className="text-gray-700 hover:text-indigo-600">Add Entry</Link>
                  <button
                    onClick={handleLogout}
                    className="flex items-center text-gray-700 hover:text-indigo-600"
                  >
                    <LogOut className="h-5 w-5 mr-1" />
                    Logout
                  </button>
                </>
              ) : (
                <>
                  <Link to="/login" className="text-gray-700 hover:text-indigo-600">Login</Link>
                  <Link to="/register" className="text-gray-700 hover:text-indigo-600">Register</Link>
                </>
              )}
            </div>
          </div>
        </div>
      </nav>
      <main className="max-w-7xl mx-auto py-6 sm:px-6 lg:px-8">
        <Outlet />
      </main>
    </div>
  );
}